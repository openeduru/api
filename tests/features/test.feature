
Feature: Openedu.ru external Open-API step-by-step
  # https://confluence.npoed.ru/pages/viewpage.action?pageId=4161567

  Vasiliy are master of testor
  Vasiliy wants that all is work sane
  so that shitn't brix

  Scenario Outline: Авторизация API
    Given any user wants to be Vasiliy
     When request "<url>" with login "<login>" and password "<password>"
     Then server returns username "<username>" & role "<role>"
    Examples:
      | url | login | password | username | role |
      | url | login | password | username | role |

  Scenario Outline: Get info
    Given step "<desc>"
    When Vasiliy <method> url "<url>" with params "<params>"
    Then server response data according schema "<schema>"

    Examples: Пользователь
      |  desc  |  method | url | params | schema |
      | Получить информацию о пользователе  | GET | /api/user/v0/accounts/ | openedu.ru/             | user_info |
      | Получить информацию о пользователе  | GET | /api/user/v0/accounts/ | openedu.ru/?view=shared | user_info |

    Examples: Запись на курс
      |  desc  |  method | url | params | schema |
      | Получить статус записи на курс      | GET | /api/enrollment/v1/enrollment/ | openedu.ru,1 | course_status |
      # откуда вылезло user_id???
      | Получить детали записи на курс      | GET | /api/enrollment/v1/course/ | {course_id} | course_detail |
      | Просмотреть курсы, на которые записан пользователь | GET | /api/enrollment/v1/enrollment |  |  |

    Examples: Прохождение курса
      |  desc  |  method | url | params | schema |
      | Получить список курсов | GET | /api/course_structure/v1/courses/ | ?page_size=50 | courses_list |



#  Scenario Outline: Change info
#    # три сценария. изменения своей инфы, чужой инфы, невалидные значения своей инфы
#    # НБ: TODO: необходимо удалить сценарий/возможность изменения чужой инфы
#
#    Given step "<desc>"
##    And params "<params>"
#    When Vasiliy <method> url "<url>" with params "<params>"
#    Then server response "<code>"
#
#    Examples: PATH
#      |  desc  |  method | url | params | schema |
#      | Изменить информацию о пользователе | PATCH | /api/user/v0/accounts/ | openedu.ru/?view=shared | user_info |
#
#  Scenario Outline: Save info
#
#    Given step "<desc>"
##    And params "<params>"
#    When Vasiliy <method> url "<url>" with params "<params>"
#    Then server response "<code>"
#
#    Examples: POST
#      |  desc  |  method | url | params | schema |
#      | Записать пользователя на курс | POST | /api/enrollment/v1/enrollment | {"mode”: "honor”, "course_details”:{"course_id”: "edX/DemoX/Demo_Course”}} |  |
#
