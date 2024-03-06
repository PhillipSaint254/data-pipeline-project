import os

DB_DETAILS = {
    "main": {
        "SOURCE_DB": {
            "DB_TYPE": "mysql",
            "DB_HOST": "",
            "DB_NAME": "retail_db",
            "SOURCE_DB_USER": os.environ.get("SOURCE_DB_USER"),
            "SOURCE_DB_PASS": os.environ.get("SOURCE_DB_PASS"),
        },
        "TARGET_DB": {
            "DB_TYPE": 'postgres',
            "DB_HOST": '',
            "DB_NAME": 'retail_db',
            "TARGET_DB_USER": os.environ.get("TARGET_DB_USER"),
            "TARGET_DB_PASS": os.environ.get("TARGET_DB_PASS"),
        }
    }
}
