# Start with an official Nginx base image
FROM nginx:1.19-alpine

# Set a label to mark the image with metadata
LABEL maintainer="your-email@example.com"
LABEL version="1.19"
LABEL description="Nginx 1.19 with vulnerability scanning enabled"

# Set up a directory for Nginx config if needed
RUN mkdir /etc/nginx/conf.d

# Copy custom Nginx configuration (if you have any custom configurations)
# COPY nginx.conf /etc/nginx/nginx.conf

# Expose necessary ports
EXPOSE 80 443

# Default command to run Nginx
CMD ["nginx", "-g", "daemon off;"]
