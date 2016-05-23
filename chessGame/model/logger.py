import logging
#파이썬 표준 라이브러리 logging
#스트림과 파일에 동시에 로그를 남길 수 있다.
#또한 테스트 환경과 프로덕션 환경에서 남기는 로깅의 레벨이 다른 장점이 있다.
#D로깅정보는 로그의 레벨에 따라서 출력한다.
#DEBUG > INFO > WARRING > ERROR > Critical

# logger 인스턴스를 생성 및 로그 레벨 설정.
logger = logging.getLogger('root')
logger.setLevel(logging.DEBUG)

#파일로 남기기 위해서 filename (=format)을 parameter로 추가 가능하다.
#formater생성
FORMAT = "%(levelname)s: [%(filename)s:%(lineno)s - %(funcName)10s() ] %(message)s"
#원하는 format 내용을 log로 출력 
logging.basicConfig(format=FORMAT)


