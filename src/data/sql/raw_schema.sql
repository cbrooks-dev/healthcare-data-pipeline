-- Schema for raw ingested data
CREATE TABLE patient_raw (
    name TEXT,
    age INT,
    gender TEXT,
    blood_type TEXT,
    medical_condition TEXT,
    date_of_admission DATE,
    doctor TEXT,
    hospital TEXT,
    insurance_provider TEXT,
    billing_amount DECIMAL,
    room_number INT,
    admission_type TEXT,
    discharge_date DATE,
    medication TEXT,
    test_results TEXT
);
