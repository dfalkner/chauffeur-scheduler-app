# Chauffeur Scheduler Application Specifications
## Introduction
This document provides a detailed specification for the Chauffeur Scheduler Application, designed for effective management and coordination between different user roles: system administrators, dispatchers, and chauffeurs.

## User Roles and Functionalities
### System Administrators
- **Access:** Full administrative rights to all app features and configurations.
- **Responsibilities:**
  - Create and manage chauffeur and dispatcher accounts.
  - Establish and modify organizations, moving users between them.
  - Define and edit vehicle types.
  - Daily app access with secure credentials.

### Dispatchers
- **Affiliation:** Belong to an organization.
- **Access:** Yearly credential verification.
- **Capabilities:**
  - Manage and edit their organization's schedules.
  - Invite chauffeurs for self-registration.
  - View and manage chauffeur schedules and responses.
  - Assign opportunities to chauffeurs in priority order.
  - Create, update, delete (CRUD) opportunities.
  - Maintain a history of chauffeuring requests and outcomes.
  - Provide ratings and feedback post-completion of an opportunity.
  - Cancel accepted opportunities, notifying chauffeurs and dispatchers.

### Chauffeurs
- **Access Requirement:** Yearly login with credentials.
- **Capabilities:**
  - Account creation upon invitation acceptance.
  - Option to accept or reject chauffeuring opportunities, with dispatcher notification.
  - Access to personal schedules and details of accepted opportunities across organizations.
  - Document a history of opportunities, including personal notes, feedback received, and specific details.
  - Note creation for each accepted or declined opportunity.
  - Record and update opportunity statuses, such as 'picked-up' and 'dropped-off'.
  - Password reset functionality.

### System Functionality
- Facilitates communication between dispatchers and chauffeurs, maintaining a history of all chauffeuring requests, both accepted and declined.

### Notification System
- **Primary Mode:** Email notifications.
- **Future Plans:** Introduction of SMS notifications.

### Technology Stack
- **User Authentication:** AWS Cognito for secure access.
- **Web Application Framework:** Flask for versatile web development.
- **Database Storage:** Amazon RDS with PostgreSQL.
- **Email Notifications:** Amazon Simple Email Service (SES).
- **Application Backend:** AWS Lambda for serverless computing.
- **Data Security:** AWS IAM for secure access control.
- **Deployment:** AWS Elastic Beanstalk for easy deployment.
- **Version Control:** GitHub for code repository hosting.

## User Stories
### Dispatcher User Story
- **Application Access:** Via web browser on various devices.
- **Service Request Management:** Completion and submission of detailed service request forms.
- **Opportunity Tracking:** Viewing and editing opportunities and chauffeur histories.
- **Feedback Provision:** Email notifications for completed opportunities and feedback submission.

### Chauffeur User Story
- **Opportunity Reception:** Email alerts for new requests with response options.
- **Schedule Management**: Access to offered opportunities, accepted or declined, with timestamps and details.
- **Status Updates:** Updating and tracking opportunity statuses, visible to dispatchers.

## Entity and Relationship Definitions

### Key Entities
- **User:** Basic identification and role information.
  - Attributes: ID, Email, Role (System Administrator, Dispatcher, Chauffeur)
  
- **Organization:** Details about the entity, including contact and type.
  - Attributes: ID, Name, Contact Information, Website, Type (Chauffeur Organization, Dispatcher Organization)

- **Chauffeur (extends User)**: Specific details for chauffeurs, linking them to organizations and vehicles.
    - Attributes: ID, OrganizationID, Profile Photo, Driver License Number, Contact Information, Visibility (Option to be visible to all organizations)

- **Vehicle:** Information related to vehicles operated by chauffeurs.
  - Attributes: ID, ChauffeurID, Make, Model, Color, Year, Number of Seats, License Plate, VIN, Condition, Description
  
- **Opportunity**: Characteristics and status of chauffeuring assignments.
  - Attributes: ID, Status (e.g., Open, Accepted, Completed), Compensation Terms (Optional), Details

### Relationships
- **Chauffeur and Organization**: Each chauffeur is associated with one organization, but can access and manage multiple vehicles.
- **Organization and Chauffeur**: An organization can encompass multiple chauffeurs, each with their unique profiles and vehicle associations.
- **Chauffeur and Vehicle**: A chauffeur can be linked to multiple vehicles, but each vehicle is specifically assigned to one chauffeur.
- **Opportunity and Chauffeur**: Opportunities are offered to chauffeurs based on organizational needs and chauffeur availability. An opportunity is accepted by a single chauffeur but can be offered to many in a priority sequence until acceptance.

### System Integration and Functionality
- **User Authentication and Management**: Utilizing AWS Cognito, the system ensures secure and distinct access for system administrators, dispatchers, and chauffeurs. Password reset options are available for dispatchers and chauffeurs.
- **Opportunity Management**: The system allows dispatchers to create, assign, and manage opportunities, which are then available to chauffeurs. Chauffeurs can accept or reject these opportunities, with updates being communicated back to the dispatchers.
- **Communication**: The system facilitates direct communication between dispatchers and chauffeurs, primarily through email notifications. Future enhancements will incorporate SMS for broader communication options.
- **Record Keeping and Visibility**: A comprehensive history of opportunities, including their acceptance, rejection, and feedback, is maintained. Chauffeurs have visibility across multiple organizations, while dispatchers manage opportunities within their specific organization.
- **Vehicle Management**: Dispatchers have the ability to filter and search for vehicles based on various attributes, aiding in the efficient selection of chauffeurs for specific opportunities.

This comprehensive entity and relationship framework is designed to ensure that the Chauffeur Scheduler Application is efficient, user-friendly, and adaptable to the evolving needs of its users.