# Add full text search to TakeNews project with ElasticSearch
## services:
- Django REST Framework
- Docker
- Redis
- Celery
- Selenium
- Elastic Search
<hr>
<h2> urls: </h2>
<table>
  <tr>
    <th> Description </th>
    <th> Url </th>
  </tr>
  <tr>
    <td> List of news </td>
    <td> "/" </td>
  </tr>
  <tr>
    <td> Admin page </td>
    <td> "admin/" </td>
  </tr>
  <tr>
    <td> Django REST framework Api page </td>
    <td> "api/" </td>
  </tr>
  <tr>
    <td> Search news based on Tags </td>
    <td> "api/?search=(string)" </td>
  </tr>
  <tr>
    <td> Search news based on Content [elasticsearch] </td>
    <td> "search/(string)" </td>
  </tr>
  <tr>
    <td> Search news based on ID </td>
    <td> "(id)/" </td>
  </tr>
</table>
<hr>

##  Installation

- You must have Docker installed on your system

- Make a git clone or download it in zip:
    ```bash
    git clone https://github.com/pourya22334415/RoshanInternship.git
    ```

- Get in the project directory:
    ```bash
    cd RoshanInternship/TakeNews
    ```
- Run docker-compose file:
    ```bash
    docker-compose up
    ```

- To Create an admin user:
    ```bash
    # After executing the previous command, in another terminal:
    docker exec -it django sh
    # Then run this command:
    python manage.py createsuperuser
    ```

