# steptech_assignment

## Hello users to run the steptech_assignment flask program we need to do certain steps

### Environment Setup: 
#### Install Python 3.x on your machine.
> https://www.python.org/downloads/release/python-3115/
#### Then Create a python Virtual Enviorment 
> python3 -m venv name_of_virtualenv
#### Activate Virtual Enviorment
> name_of_virtualenv\scripts\activate.bat
#### Install required libraries to run the project
> pip install -r requirements.txt

#### Execute following query on mysql to create and steup database and tables

CREATE DATABASE users
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";
CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;


