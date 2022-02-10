provider "aws" {
  profile    = "default"
  region     = "eu-west-3"
}

variable "key_pair_path" {
  type = map(string)
  default = {
    public_key_path = "~/.ssh/id_rsa.pub"
  }
}

resource "aws_instance" "staging-app" {
  ami           = "ami-06ad2ef8cd7012912"
  key_name      = "deploy-key"
  instance_type = "t2.micro"
    tags = {
    Name = "Staging-ClickCount"
  }
  root_block_device {
    volume_size           = "20"
    volume_type           = "standard"
    delete_on_termination = "true"
  }
  provisioner "local-exec" {
    command = "ansible-playbook -i '${self.public_ip},' playbook.yml --extra-vars ipv4='${self.public_ip}'"
  }
}

resource "aws_instance" "production-app" {
  ami           = "ami-06ad2ef8cd7012912"
  key_name      = "deploy-key"
  instance_type = "t2.micro"
    tags = {
    Name = "Production-ClickCount"
  }
    root_block_device {
    volume_size           = "20"
    volume_type           = "standard"
    delete_on_termination = "true"
  }
  provisioner "local-exec" {
    command = "ansible-playbook -i '${self.public_ip},' playbook.yml --extra-vars ipv4='${self.public_ip}'"
  }
}

resource "aws_key_pair" "deploy-key" {
  key_name   = "deploy-key"
  public_key = file(var.key_pair_path["public_key_path"])
}

resource "aws_default_vpc" "clickcount-vpc" {
  tags = {
    Name = "Clickcount VPC"
  }
}

resource "aws_default_security_group" "default" {
  vpc_id = aws_default_vpc.clickcount-vpc.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# resource "aws_elasticache_cluster" "staging-cache" {
#   cluster_id           = "cluster-staging"
#   engine               = "redis"
#   node_type            = "cache.t2.micro"
#   num_cache_nodes      = 1
#   parameter_group_name = "default.redis3.2"
#   engine_version       = "3.2.10"
#   port                 = 6379
# }

# resource "aws_elasticache_cluster" "production-cache" {
#   cluster_id           = "cluster-production"
#   engine               = "redis"
#   node_type            = "cache.t2.micro"
#   num_cache_nodes      = 1
#   parameter_group_name = "default.redis3.2"
#   engine_version       = "3.2.10"
#   port                 = 6379
# }
