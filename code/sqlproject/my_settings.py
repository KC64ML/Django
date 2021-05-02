DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'studydb',  # DB명
        'USER': 'root',    # DB 계정
        'PASSWORD': '1234',  # 계정 비밀번호
        'HOST': 'localhost',    # 데이터베이스 주소(IP)
        'PORT': '3306',         # 데이터베이스 포트(보통 3306)
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}
