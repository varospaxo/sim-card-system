CREATE TABLE sim_card (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    sim_number VARCHAR(20) NOT NULL UNIQUE,
    phone_number VARCHAR(15) NOT NULL,
    status ENUM('active', 'inactive') NOT NULL,
    activation_date TIMESTAMP NULL
);
