FROM nginx:1.27.3-alpine-slim

# Set a secure working directory
WORKDIR /usr/share/nginx/html

# Copy static content into the container
COPY index.html .

# Remove unnecessary files from the image to minimize size and vulnerabilities
RUN rm -rf /var/cache/apk/* /tmp/* /var/tmp/*

# Expose Nginx port
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
