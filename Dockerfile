FROM python:3.9-alpine3.13
LABEL maintainer="recipe_app_api"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install python-dotenv && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    # adding new user, that's the best practice not using the root user \
    # don't run your app using the root user
    adduser \
        --disabled-password \
        # no creating home directory for that user to make image as lightweight as possible
        --no-create-home \
        # specifying the name of the user
        django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    # chown - change owner
    chown -R django-user:django-user /vol && \
    # chmod - change mode
    chmod -R 755 /vol


ENV PATH="/py/bin:$PATH"

# specifying the user that we switching to
USER django-user
