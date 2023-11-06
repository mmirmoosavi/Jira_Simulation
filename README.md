# Jira-Like Task Management System

This project is a Jira-like task management system built with Django, designed to handle a large number of tasks
efficiently. The system includes a flexible custom field feature, making it suitable for companies and organizations
with extensive task management needs.

## Database Choice: PostgreSQL

We have chosen PostgreSQL as the database for this project due to several reasons:

- **Scalability**: PostgreSQL is well-known for its ability to handle large datasets efficiently, making it a suitable
  choice for managing tasks, especially when dealing with a significant number of records.

- **Data Integrity**: PostgreSQL offers robust data integrity and constraint enforcement, which is crucial for
  maintaining data quality in a task management system.

- **Extensibility**: PostgreSQL supports custom data types, which aligns well with our custom field requirements.

- **Community Support**: It has a strong and active open-source community, ensuring ongoing support, security updates,
  and the availability of extensions and add-ons.

- **SQL Support**: PostgreSQL fully supports SQL standards, making it easier to work with the database and integrate
  with other tools.

- **Data Types**: PostgreSQL offers a wide range of built-in data types and allows you to create custom data types,
  which aligns well with our requirement for custom field types.

- **Django Compatibility**: Django, the high-level Python web framework used in this project, has excellent support for
  PostgreSQL, enabling us to leverage its advanced features seamlessly.

# Database Considerations

When developing and managing a database for a project like this, there are several key considerations to ensure the system's reliability, performance, and scalability:

1. **Indexes**: Create appropriate indexes on frequently queried fields in both the Tasks and Custom Fields tables to improve query performance. Well-designed indexes can significantly enhance the speed of data retrieval.

2. **Normalization**: Ensure your table structure is normalized to minimize data redundancy and improve data integrity. This includes organizing your data into related tables to prevent anomalies and ensure consistency.

3. **Scalability**: Be prepared to use partitioning and sharding techniques as your dataset grows, especially if you're expecting millions of tasks. These strategies will help distribute data across multiple servers and keep the system responsive.

4. **Caching**: Implement caching mechanisms to reduce database load, especially for frequently accessed data. Caching can greatly improve response times by serving data from memory instead of making frequent database queries.

5. **Query Optimization**: Use proper query optimization techniques and regularly analyze query performance to make necessary adjustments. This includes optimizing SQL queries, considering database indexes, and reducing query load.

6. **Backup and Recovery**: Implement robust backup and recovery strategies to safeguard your data. Regular backups and disaster recovery plans are essential to protect against data loss and system downtime.

7. **Security**: Ensure proper access control, data encryption, and other security measures to protect your data and comply with data protection regulations. Protect sensitive data and control access to maintain data privacy and security.

8. **Testing**: Thoroughly test your database structure with a representative dataset and expected usage patterns to identify potential bottlenecks and performance issues. Comprehensive testing is critical to ensuring the system's stability and performance under real-world conditions.

By addressing these considerations, you can create a reliable and high-performing database system for your Jira-like task management project.


## Models

### Task

The `Task` model represents a task with the following fields:

- `id`: Unique identifier for the task.
- `name`: Name or title of the task.
- `description`: Description of the task.
- `status`: The current status of the task (e.g., open, in progress, closed).
- Other static fields...

### CustomField

The `CustomField` model represents custom fields for tasks and includes the following fields:

- `id`: Unique identifier for the custom field.
- `task`: Foreign key to the associated task.
- `field_name`: Name of the custom field.
- `field_type`: The type of the custom field (text, integer, date, user, etc.).
- `field_value_text`: Text value for the custom field.
- `field_value_int`: Integer value for the custom field.
- `field_value_date`: Date value for the custom field.
- `field_value_user`: Foreign key to the associated user (if the field is a user link).

### User

The `User` model represents user information, and it is used to link tasks to users.

## Getting Started

## Table of Contents

- [Features](#features)
- [Getting Started with Docker](#getting-started-with-docker)


## Features

- Create, read, update, and delete tasks.
- Define custom fields with different data types (text, integer, date, user links, etc.).
- Filter and search tasks by various criteria, including static and custom fields.
- Scalable and suitable for managing a large number of tasks.
- Built using Django, a high-level Python web framework.

## Getting Started with Docker

To run this project with Docker, follow these steps:

1. Clone the repository.

2. Make sure you have Docker and Docker Compose installed on your system.

3. Open a terminal and navigate to the project directory.

4. Build and start the Docker containers using the following command.

    * docker-compose up --build -d

5. Apply migrations and create a superuser to access the admin interface.

    * docker-compose exec jira_api python manage.py migrate

    * docker-compose exec jira_api python manage.py createsuperuser

6. You can now access the project at `http://localhost:9000` and the admin interface at `http://localhost:9000/admin`.
