terraform {
    required_providers {
        docker = {
            source = "kreuzwerker/docker"
            version = "2.16.0"
        }
    }
}

provider "docker" {
    host = "unix:///var/run/docker.sock"
}

# Pull Jenkins image
resource "docker_image" "jenkins" {
    name = "jenkins/jenkins:lts-jdk11"
}

# Creates a container
resource "docker_container" "jenkins" {
    image = docker_image.jenkins.latest
    name = "jenkins"
    ports {
        internal = 8080
        external = 8080
    }
    ports {
        internal = 50000
        external = 50000
    }
    volumes {
        container_path = "/var/jenkins_home"
        host_path = "/jenkins_home"
    }
    tty = true
}