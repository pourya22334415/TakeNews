# Implementation of REST API
<hr>
<h3><li><a href="http://pouryakarami.pythonanywhere.com/"> PythonAnyWhere Link </a></li></h3>
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
    <td> "api/?search=(string) </td>
  </tr>
  <tr>
    <td> Search news based on ID </td>
    <td> "(id)/" </td>
  </tr>
</table>
<hr>

##  Installation

- Make a git clone or download it in zip:
    ```bash
    git clone https://github.com/pourya22334415/RoshanInternship.git
    ```

- Get in the directory:
    ```bash
    cd RoshanInternship
    ```

- Install from your terminal with pip requirements.txt:
    ```bash
    pip install -r requirements.txt
    ```
    
- Create new migrations based on the changes you have made to your models:
    ```bash
    cd TakeNews
    python manage.py makemigrations
    ```

- Apply migrations:
    ```bash
    python manage.py migrate
    ```

- To Create an admin user:
    ```bash
    python manage.py createsuperuser
    ```
