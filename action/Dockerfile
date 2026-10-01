FROM python:3.14-alpine3.23

# Setup base
RUN \
    apk add --no-cache \
        bash \
        git \
    \
    && pip3 install \
        --no-cache-dir \
        --prefer-binary \
        --find-links "https://wheels.home-assistant.io/musllinux/" \
        "repository-updater @ git+https://github.com/killer0071234/repository-updater@11f2cc8eed0c84a2cade458d652b9ab2e7b81a0f"

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
