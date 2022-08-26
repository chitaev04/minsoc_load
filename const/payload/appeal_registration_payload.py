import random
from auxiliary_func import random_parameter_bool, DictValues, FileGet, give_tomorrow_date


class DictParametrs(DictValues):

    def registration_body_content_additions(self):
        registration_body_put_part1 = {
            "attrValues":
                {
                    "sstuIsUploaded":
                        {
                            "attr":
                                {
                                    "name": "Выгружено в ССТУ",
                                    "attributeType":
                                        {
                                            "bool": True
                                        }
                                },
                            "value": False
                        },
                    "sstuStatus":
                        {
                            "attr":
                                {
                                    "name": "Статус ССТУ",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryStatus":
                        {
                            "attr":
                                {
                                    "name": "Статус",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value":
                                {
                                    "id": "07BFCE5B-EE9F-42C3-BEFE-2F7A75B7CDAD",
                                    "name": "Отложенные при регистрации",
                                    "mnemonic": "inquiryPostponed",
                                    "extraName": "Отложенные при регистрации",
                                    "viewOrder": 0,
                                    "infoPanel": "Docflow.info.StatusInfoPanel",
                                    "entityClass": "su.opencode.docflow.documents.domain.StatusEntity"
                                }
                        },
                    "inquiryAddressee":
                        {
                            "attr":
                                {
                                    "name": "Адресат",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value":
                                {
                                    "id": "31DEE17A-DE15-40CF-8F01-5EBF3F025282",
                                    "name": "Заявитель",
                                    "extraName": "Заявитель",
                                    "viewOrder": 0,
                                    "version": 16,
                                    "entityClass": "su.opencode.docflow.documents.domain.doc.DocumentEntity"
                                }
                        },
                    "inquiryAddresseeSigner":
                        {
                            "attr":
                                {
                                    "name": "Фамилия подписавшего",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryAddresseeOutNum":
                        {
                            "attr":
                                {
                                    "name": "Исходящий номер",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryAddresseeOutNumPres":
                        {
                            "attr":
                                {
                                    "name": "Исходящий номер Адм. Президента",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryAddresseeDate":
                        {
                            "attr":
                                {
                                    "name": "Дата запроса",
                                    "attributeType":
                                        {
                                            "date": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryType":
                        {
                            "attr":
                                {
                                    "name": "Тип обращения",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "Письменное"
                        },
                    "inquirySourceOfDocument":
                        {
                            "attr":
                                {
                                    "name": "Источник поступления",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "Письменно"
                        },
                    "inquiryAppealType":
                        {
                            "attr":
                                {
                                    "name": "Вид обращения",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "Заявление"
                        },
                    "inquiryRiddle":
                        {
                            "attr":
                                {
                                    "name": "Рассмотрение по ФЗ",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "ФЗ-59"
                        },
                    "inquiryPreTrialAppeal":
                        {
                            "attr":
                                {
                                    "name": "Досудебное обжалование предоставления госуслуги",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "Нет"
                        },
                    "inquiryRegNumber":
                        {
                            "attr":
                                {
                                    "name": "Рег. номер",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryRepetition":
                        {
                            "attr":
                                {
                                    "name": "Повторность",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryReasonForReAppeal":
                        {
                            "attr":
                                {
                                    "name": "Причина повторного обращения",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryCollectiveAppeal":
                        {
                            "attr":
                                {
                                    "name": "Коллективное обращение",
                                    "attributeType":
                                        {
                                            "bool": True
                                        }
                                },
                            "value": False
                        },
                    "inquiryIsSpecialControl":
                        {
                            "attr":
                                {
                                    "name": "На особый контроль (2К)",
                                    "attributeType":
                                        {
                                            "bool": True
                                        }
                                },
                            "value": False
                        },
                    "inquiryIsCorruption":
                        {
                            "attr":
                                {
                                    "name": "Коррупция",
                                    "attributeType":
                                        {
                                            "bool": True
                                        }
                                },
                            "value": False
                        },
                    "inquiryCreateDate":
                        {
                            "attr":
                                {
                                    "name": "Дата поступления",
                                    "attributeType":
                                        {
                                            "date": True
                                        }
                                },
                            "value": 1657742400000
                        },
                    "inquiryRegDate":
                        {
                            "attr":
                                {
                                    "name": "Дата регистрации",
                                    "attributeType":
                                        {
                                            "date": True
                                        }
                                },
                            "value": 1657742400000
                        },
                    "inquiryDurationInDays":
                        {
                            "attr":
                                {
                                    "name": "Длительность (в днях)",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "30"
                        },
                    "inquiryDateFinish":
                        {
                            "attr":
                                {
                                    "name": "Срок исполнения",
                                    "attributeType":
                                        {
                                            "date": True
                                        }
                                },
                            "value": 1660248000000
                        },
                    "inquiryAnotation":
                        {
                            "attr":
                                {
                                    "name": "Примечание",
                                    "attributeType":
                                        {
                                            "longString": True
                                        }
                                },
                            "value": None
                        },
                    "isPostSendingMethod":
                        {
                            "attr":
                                {
                                    "name": "Почтовое отправление",
                                    "attributeType":
                                        {
                                            "bool": True
                                        }
                                },
                            "value": False
                        },
                    "isEmailSendingMethod":
                        {
                            "attr":
                                {
                                    "name": "Электронная почта",
                                    "attributeType":
                                        {
                                            "bool": True
                                        }
                                },
                            "value": False
                        },
                    "isPersonalSendingMethod":
                        {
                            "attr":
                                {
                                    "name": "Выдача на руки",
                                    "attributeType":
                                        {
                                            "bool": True
                                        }
                                },
                            "value": False
                        },
                    "identityVerified":
                        {
                            "attr":
                                {
                                    "name": "Личность подтверждена",
                                    "attributeType":
                                        {
                                            "bool": True
                                        }
                                },
                            "value": False
                        },
                    "inquiryLastname":
                        {
                            "attr":
                                {
                                    "name": "Фамилия",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryFirstname":
                        {
                            "attr":
                                {
                                    "name": "Имя",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquirySecondname":
                        {
                            "attr":
                                {
                                    "name": "Отчество",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "externalSystemAddress":
                        {
                            "attr":
                                {
                                    "name": "Адрес из внешней системы",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryNonresident":
                        {
                            "attr":
                                {
                                    "name": "Иногородние",
                                    "attributeType":
                                        {
                                            "bool": True
                                        }
                                },
                            "value": False
                        },
                    "inquiryTerritoryRef":
                        {
                            "attr":
                                {
                                    "name": "Территория",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryFederalSubject":
                        {
                            "attr":
                                {
                                    "name": "Субъект РФ",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "обл. Самарская"
                        },
                    "inquirySettlement":
                        {
                            "attr":
                                {
                                    "name": "Поселение/Внутригородской район",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryStreet":
                        {
                            "attr":
                                {
                                    "name": "Улица",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryHouseNumber":
                        {
                            "attr":
                                {
                                    "name": "Дом",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryRoomNumber":
                        {
                            "attr":
                                {
                                    "name": "Квартира",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "externalSystemAddressId":
                        {
                            "attr":
                                {
                                    "name": "ID адреса из внешней системы",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryDistrict":
                        {
                            "attr":
                                {
                                    "name": "Областной район/Внутригородской округ",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryLocality":
                        {
                            "attr":
                                {
                                    "name": "Город/Населенный пункт",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryTerritory":
                        {
                            "attr":
                                {
                                    "name": "Элемент план. структуры",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryStead":
                        {
                            "attr":
                                {
                                    "name": "Участок",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryPostcode":
                        {
                            "attr":
                                {
                                    "name": "Индекс",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryBuildingHouse":
                        {
                            "attr":
                                {
                                    "name": "Корпус",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "federalSubjectId":
                        {
                            "attr":
                                {
                                    "name": "ID Субъекта РФ",
                                    "attributeType":
                                        {
                                            "numeric": True
                                        }
                                },
                            "value": 1121548
                        },
                    "settlementId":
                        {
                            "attr":
                                {
                                    "name": "ID Поселения",
                                    "attributeType":
                                        {
                                            "numeric": True
                                        }
                                },
                            "value": None
                        },
                    "territoryId":
                        {
                            "attr":
                                {
                                    "name": "ID Элемента планировочной структуры",
                                    "attributeType":
                                        {
                                            "numeric": True
                                        }
                                },
                            "value": None
                        },
                    "steadId":
                        {
                            "attr":
                                {
                                    "name": "ID Участка",
                                    "attributeType":
                                        {
                                            "numeric": True
                                        }
                                },
                            "value": None
                        },
                    "apartmentId":
                        {
                            "attr":
                                {
                                    "name": "ID Квартиры",
                                    "attributeType":
                                        {
                                            "numeric": True
                                        }
                                },
                            "value": None
                        },
                    "districtId":
                        {
                            "attr":
                                {
                                    "name": "ID Района",
                                    "attributeType":
                                        {
                                            "numeric": True
                                        }
                                },
                            "value": None
                        },
                    "localityId":
                        {
                            "attr":
                                {
                                    "name": "ID Населенного пункта",
                                    "attributeType":
                                        {
                                            "numeric": True
                                        }
                                },
                            "value": None
                        },
                    "streetId":
                        {
                            "attr":
                                {
                                    "name": "ID Улицы",
                                    "attributeType":
                                        {
                                            "numeric": True
                                        }
                                },
                            "value": None
                        },
                    "houseId":
                        {
                            "attr":
                                {
                                    "name": "ID Дома",
                                    "attributeType":
                                        {
                                            "numeric": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryEmail":
                        {
                            "attr":
                                {
                                    "name": "Адрес электронной почты",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryAttachedTo":
                        {
                            "attr":
                                {
                                    "name": "Подвед. организация",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryAssistants":
                        {
                            "attr":
                                {
                                    "name": "Сопровождающие лица",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryOrganization":
                        {
                            "attr":
                                {
                                    "name": "Юр.лицо",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryPhoneNumber":
                        {
                            "attr":
                                {
                                    "name": "Телефон",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquirySNILS":
                        {
                            "attr":
                                {
                                    "name": "СНИЛС",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryBirthDate":
                        {
                            "attr":
                                {
                                    "name": "Дата рождения",
                                    "attributeType":
                                        {
                                            "date": True
                                        }
                                },
                            "value": None
                        },
                    "inquirySocialCategories":
                        {
                            "attr":
                                {
                                    "name": "Социальные категории",
                                    "attributeType":
                                        {
                                            "list": True
                                        }
                                },
                            "value":
                                []
                        },
                    "collective":
                        {
                            "attr":
                                {
                                    "name": "Коллективное",
                                    "attributeType":
                                        {
                                            "bool": True
                                        }
                                },
                            "value": False
                        },
                    "caseNumber":
                        {
                            "attr":
                                {
                                    "name": "№ Дела",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "caseName":
                        {
                            "attr":
                                {
                                    "name": "Наименование дела",
                                    "attributeType":
                                        {
                                            "longString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryRealSignatory":
                        {
                            "attr":
                                {
                                    "name": "Подписант",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryQuestionList":
                        {
                            "attr":
                                {
                                    "name": "Содержание",
                                    "attributeType":
                                        {
                                            "list": True
                                        }
                                },
                            "value":
                                []
                        },
                    "showArchivedPreviousInquiries":
                        {
                            "attr":
                                {
                                    "name": "Показать архивные",
                                    "attributeType":
                                        {
                                            "bool": True
                                        }
                                },
                            "value": False
                        },
                    "inquiryReasonForPetition":
                        {
                            "attr":
                                {
                                    "name": "Меры соц.поддержки",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "attachmentSheet":
                        {
                            "attr":
                                {
                                    "name": "Количество листов вложения",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryText":
                        {
                            "attr":
                                {
                                    "name": "Комментарий",
                                    "attributeType":
                                        {
                                            "longString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryResult":
                        {
                            "attr":
                                {
                                    "name": "Результат рассмотрения",
                                    "attributeType":
                                        {
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryResultDate":
                        {
                            "attr":
                                {
                                    "name": "Дан ответ",
                                    "attributeType":
                                        {
                                            "date": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryAnswer":
                        {
                            "attr":
                                {
                                    "name": "Текст ответа",
                                    "attributeType":
                                        {
                                            "longString": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryFilesList":
                        {
                            "attr":
                                {
                                    "name": "Файлы (список)",
                                    "attributeType":
                                        {
                                            "list": True
                                        }
                                },
                            "value":
                                []
                        },
                    "inquirySourceFileList":
                        {
                            "attr":
                                {
                                    "name": "Файлы обращения (список)",
                                    "attributeType":
                                        {
                                            "list": True
                                        }
                                },
                            "value":
                                []
                        },
                    "sendOnControlDate":
                        {
                            "attr":
                                {
                                    "name": "Дата перевода На контроль",
                                    "attributeType":
                                        {
                                            "date": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryExecutionDate":
                        {
                            "attr":
                                {
                                    "name": "Фактическая дата выполнения",
                                    "attributeType":
                                        {
                                            "date": True
                                        }
                                },
                            "value": None
                        },
                    "erpDeclarant":
                        {
                            "attr":
                                {
                                    "name": "Заявитель ЕРП ",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "regCardSearchGroupDeclarantLink":
                        {
                            "attr":
                                {
                                    "name": "Заявитель",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value": None
                        },
                    "isShortVerbalRoute":
                        {
                            "attr":
                                {
                                    "name": "Это короткий устный ответ",
                                    "attributeType":
                                        {
                                            "bool": True
                                        }
                                },
                            "value": False
                        },
                    "executor":
                        {
                            "attr":
                                {
                                    "name": "Исполнитель",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "sstuUploadedDate":
                        {
                            "attr":
                                {
                                    "name": "Дата и время выгрузки в ССТУ",
                                    "attributeType":
                                        {
                                            "date": True
                                        }
                                },
                            "value": None
                        },
                    "mainInquiryQuestionsResolutionAuthor":
                        {
                            "attr":
                                {
                                    "name": "Автор резолюции главного вопроса",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value": None
                        },
                    "answerSigningDate":
                        {
                            "attr":
                                {
                                    "name": "Дата ответа",
                                    "attributeType":
                                        {
                                            "date": True
                                        }
                                },
                            "value": None
                        },
                    "closingExecutionCard":
                        {
                            "attr":
                                {
                                    "name": "Закрывающая карточка исполнения",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value": None
                        },
                    "creationDate":
                        {
                            "attr":
                                {
                                    "name": "Дата дела",
                                    "attributeType":
                                        {
                                            "date": True
                                        }
                                },
                            "value": None
                        },
                    "caseLink":
                        {
                            "attr":
                                {
                                    "name": "Выбранное дело",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value": None
                        },
                    "registrar":
                        {
                            "attr":
                                {
                                    "name": "Регистратор",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value": None
                        },
                    "rootDepartment":
                        {
                            "attr":
                                {
                                    "name": "Корневой департамент",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value":
                                {
                                    "id": "CAEB5CBF-0D66-42C3-B29C-74F0A5892AC5",
                                    "name": "ГКУ СО «Главное управление социальной защиты населения Северо-Восточного округа» ",
                                    "extraName": "ГКУ СО «Главное управление социальной защиты населения Северо-Восточного округа» ",
                                    "viewOrder": 0,
                                    "entityClass": "su.opencode.docflow.auth.domain.Department"
                                }
                        },
                    "parentInquiry":
                        {
                            "attr":
                                {
                                    "name": "Родительское обращение",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value": None
                        },
                    "requestPlace":
                        {
                            "attr":
                                {
                                    "name": "Запрос на места",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value": None
                        },
                    "declarantIDESIA":
                        {
                            "attr":
                                {
                                    "name": "ID заявителя из ЕСИА",
                                    "attributeType":
                                        {
                                            "shortString": True
                                        }
                                },
                            "value": None
                        },
                    "changeStatusOfInquiryDate":
                        {
                            "attr":
                                {
                                    "name": "Дата смены статуса",
                                    "attributeType":
                                        {
                                            "date": True
                                        }
                                },
                            "value": None
                        },
                    "fastTrack":
                        {
                            "attr":
                                {
                                    "name": "Фаст-трек",
                                    "attributeType":
                                        {
                                            "bool": True
                                        }
                                },
                            "value": False
                        },
                    "inquiryID":
                        {
                            "attr":
                                {
                                    "name": "ID",
                                    "attributeType":
                                        {
                                            "numeric": True
                                        }
                                },
                            "value": None
                        },
                    "iOrigin":
                        {
                            "attr":
                                {
                                    "name": "Источник данных",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value":
                                {
                                    "id": "7E9619AF-00EB-4027-8D31-58874735B5D7",
                                    "name": "Документ системы",
                                    "viewOrder": 0,
                                    "infoPanel": "Docflow.info.OriginInfoPanel",
                                    "entityClass": "su.opencode.docflow.documents.domain.misc.OriginEntity"
                                }
                        }
                },
            "project": False,
            "deleted": False,
            "read": False,
            "hasRestrictions": True,
            "activeTab":
                {
                    "tabMnemonic": "inquiryTabDataCommon",
                    "force": False
                },
            "alternativeDocumentViewClass": None,
            "entityClass": "su.opencode.docflow.documents.domain.doc.DocumentEntity",
            "fullId": "6291AC70-93B6-4921-A1F8-21B25212D9DBDocumentEntity",
            "actionType": "APPLY"
        }
        return registration_body_put_part1

    def registration_body_save_additions(self):
        registration_body_put_part2 = {"attrValues": {
            "inquiryQuestionList": {
                "attr": {
                    "name": "Содержание"
                },
                "value": [
                    {
                        "@rowId": "",
                        "@removed": False,
                        "@order": -1,
                        "@modified": True,
                        "sstuFullCode": "0001.0001.0001.0001",
                        "inquiryContent": {
                            "id": "FB0DC00F-F0ED-4236-B845-2D30DDC0D309"
                        },
                        "@inquiryContent_text": "",
                        "inquiryQuestion": None,
                        "@inquiryQuestion_text": ""
                    }
                ]
            }
        },
            "project": False,
            "deleted": False,
            "read": True,
            "hasRestrictions": True,
            "activeTab": {
                "tabMnemonic": "inquiryTabDataCommon",
                "force": False
            },
            "alternativeDocumentViewClass": None,
            "entityClass": "su.opencode.docflow.documents.domain.doc.DocumentEntity",
            "actionType": "APPLY"
        }
        return registration_body_put_part2

    def ask_resolution_body(self, processInstanceId_res, historyId_res, connectionId_res, question_id):
        ask_resolution_body = {"attrValues": {},
                               "project": False,
                               "deleted": False,
                               "read": False,
                               "hasRestrictions": True,
                               "activeTab": {
                                   "tabMnemonic": "inquiryTabDataCommon",
                                   "force": False
                               },
                               "alternativeDocumentViewClass": None,
                               "entityClass": "su.opencode.docflow.documents.domain.doc.DocumentEntity",
                               "processParams": {
                                   "processInstanceId": f"{processInstanceId_res}",
                                   "connectionId": f"{connectionId_res}",
                                   "historyId": f"{historyId_res}",
                                   "variantName": "Задать резолюцию и исполнителей",
                                   "votes": 1,
                                   "additionalParams": {
                                       "resolutionFormData": {
                                           "questionId": f"{question_id}",
                                           "questionResolution": "В работу",
                                           "questionResolutionDescription": "Тестовое описание резолюции",
                                           "questionPlanFinishDate": "11.04.2020",
                                           "executors": [
                                               {
                                                   "executor": {
                                                       "id": "C4740BE6-555A-4B4E-9204-38559EA64928",
                                                       "extraName": "Андреева Ольга Валерьевна - Старший инспектор",
                                                       "manager": None
                                                   },
                                                   "executorResolution": "Иные",
                                                   "executorPlanFinishDate": "11.04.2020",
                                                   "isQuestionResponsible": True
                                               }
                                           ]
                                       }
                                   }
                               },
                               "actionType": "APPLY"
                               }
        return ask_resolution_body

    def registration_body_registration(self, processInstanceId, historyId, connectionIdWriting):
        gen_str = ''.join((random.choice('АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя')
                           for i in range(10)))
        registration_body_put_part3 = {
            "attrValues":
                {
                    "inquiryAddressee":
                        {
                            "attr":
                                {
                                    "name": "Адресат",
                                    "attributeType":
                                        {
                                            "reference": True
                                        }
                                },
                            "value":
                                self.get_dict_values(attribute_name='inquiryAddressee')
                        },
                    "inquiryAddresseeSigner":
                        {
                            "attr":
                                {
                                    "name": "Фамилия подписавшего",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": self.get_dict_values(attribute_name='inquiryAddresseeSigner', name=True)
                        },
                    "inquiryAddresseeOutNum":
                        {
                            "attr":
                                {
                                    "name": "Исходящий номер",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "shortString": True
                                        }
                                },
                            "value": "12"
                        },
                    "inquiryAddresseeOutNumPres":
                        {
                            "attr":
                                {
                                    "name": "Исходящий номер Адм. Президента",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "shortString": True
                                        }
                                },
                            "value": "1"
                        },
                    "inquiryAddresseeDate":
                        {
                            "attr":
                                {
                                    "name": "Дата запроса",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "date": True
                                        }
                                },
                            "value": 1658347200000
                        },
                    "inquiryAnotation":
                        {
                            "attr":
                                {
                                    "name": "Примечание",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "longString": True
                                        }
                                },
                            "value": "Примечание"
                        },
                    "inquiryLastname":
                        {
                            "attr":
                                {
                                    "name": "Фамилия",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "shortString": True
                                        }
                                },
                            "value": "Сидоров"
                        },
                    "inquiryFirstname":
                        {
                            "attr":
                                {
                                    "name": "Имя",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "shortString": True
                                        }
                                },
                            "value": "Анатолий"
                        },
                    "inquirySecondname":
                        {
                            "attr":
                                {
                                    "name": "Отчество",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "shortString": True
                                        }
                                },
                            "value": "Иванович"
                        },
                    "inquiryFederalSubject":
                        {
                            "attr":
                                {
                                    "name": "Субъект РФ",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "обл. Самарская"
                        },
                    "inquirySettlement":
                        {
                            "attr":
                                {
                                    "name": "Поселение/Внутригородской район",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "с.п. Бобровка"
                        },
                    "inquiryStreet":
                        {
                            "attr":
                                {
                                    "name": "Улица",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "ул. Кирова"
                        },
                    "inquiryHouseNumber":
                        {
                            "attr":
                                {
                                    "name": "Дом",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "д. 125"
                        },
                    "inquiryRoomNumber":
                        {
                            "attr":
                                {
                                    "name": "Квартира",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "5"
                        },
                    "inquiryDistrict":
                        {
                            "attr":
                                {
                                    "name": "Областной район/Внутригородской округ",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "м.р-н Кинельский"
                        },
                    "inquiryLocality":
                        {
                            "attr":
                                {
                                    "name": "Город/Населенный пункт",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "с. Бобровка"
                        },
                    "inquiryTerritory":
                        {
                            "attr":
                                {
                                    "name": "Элемент план. структуры",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "тер. СНТ Флора-2"
                        },
                    "inquiryStead":
                        {
                            "attr":
                                {
                                    "name": "Участок",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "з/у 25"
                        },
                    "inquiryPostcode":
                        {
                            "attr":
                                {
                                    "name": "Индекс",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "shortString": True
                                        }
                                },
                            "value": "446406"
                        },
                    "federalSubjectId":
                        {
                            "attr":
                                {
                                    "name": "ID Субъекта РФ",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "numeric": True
                                        }
                                },
                            "value": 1121548
                        },
                    "settlementId":
                        {
                            "attr":
                                {
                                    "name": "ID Поселения",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "numeric": True
                                        }
                                },
                            "value": 95248268
                        },
                    "territoryId":
                        {
                            "attr":
                                {
                                    "name": "ID Элемента планировочной структуры",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "numeric": True
                                        }
                                },
                            "value": 1146570
                        },
                    "steadId":
                        {
                            "attr":
                                {
                                    "name": "ID Участка",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "numeric": True
                                        }
                                },
                            "value": 84993826
                        },
                    "districtId":
                        {
                            "attr":
                                {
                                    "name": "ID Района",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "numeric": True
                                        }
                                },
                            "value": 95248266
                        },
                    "localityId":
                        {
                            "attr":
                                {
                                    "name": "ID Населенного пункта",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "numeric": True
                                        }
                                },
                            "value": 1137777
                        },
                    "streetId":
                        {
                            "attr":
                                {
                                    "name": "ID Улицы",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "numeric": True
                                        }
                                },
                            "value": None
                        },
                    "houseId":
                        {
                            "attr":
                                {
                                    "name": "ID Дома",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "numeric": True
                                        }
                                },
                            "value": None
                        },
                    "inquiryAssistants":
                        {
                            "attr":
                                {
                                    "name": "Сопровождающие лица",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "shortString": True
                                        }
                                },
                            "value": "Сидоров"
                        },
                    "inquiryOrganization":
                        {
                            "attr":
                                {
                                    "name": "Юр.лицо",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "shortString": True
                                        }
                                },
                            "value": "ИП Сидоров"
                        },
                    "inquiryPhoneNumber":
                        {
                            "attr":
                                {
                                    "name": "Телефон",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "shortString": True
                                        }
                                },
                            "value": "88465699999"
                        },
                    "inquirySNILS":
                        {
                            "attr":
                                {
                                    "name": "СНИЛС",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "shortString": True
                                        }
                                },
                            "value": "789-456-123 64"
                        },
                    "inquiryBirthDate":
                        {
                            "attr":
                                {
                                    "name": "Дата рождения",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "date": True
                                        }
                                },
                            "value": 886536000000
                        },
                    "inquirySocialCategories":
                        {
                            "attr":
                                {
                                    "name": "Социальные категории",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "list": True
                                        }
                                },
                            "value":
                                [
                                    {
                                        "@rowId": None,
                                        "@removed": False,
                                        "@order": 0,
                                        "@modified": True,
                                        "inquirySocialCategory": "Инвалиды без степени ограничения способности к "
                                                                 "трудовой деятельности "
                                    }
                                ]
                        },
                    "attachmentSheet":
                        {
                            "attr":
                                {
                                    "name": "Количество листов вложения",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "shortString": True
                                        }
                                },
                            "value": "1"
                        },
                    "inquiryText":
                        {
                            "attr":
                                {
                                    "name": "Текст обращения",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "longString": True
                                        }
                                },
                            "value": "текст тестовый "
                        },
                    "inquirySourceFileList":
                        {
                            "attr":
                                {
                                    "name": "Файлы обращения (список)",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "list": True
                                        }
                                },
                            "value":
                                [
                                    {
                                        "@rowId": None,
                                        "@removed": False,
                                        "@order": -1,
                                        "@modified": False,
                                        "inquirySourceFileFile":
                                            {
                                                "id": "194D1509-ED1D-4DB8-B462-7E04F8E75F4C"
                                            },
                                        "@inquirySourceFileFile_text": "<Без имени>",
                                        "inquirySourceFileText": None
                                    }
                                ]
                        },
                    "isSearhInSys":
                        {
                            "attr":
                                {
                                    "name": "Искал в системе",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "bool": True
                                        }
                                },
                            "value": True
                        },
                    "isSearchInErp":
                        {
                            "attr":
                                {
                                    "name": "Искал в ЕРП",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "bool": True
                                        }
                                },
                            "value": True
                        },
                    "inquiryRepetition":
                        {
                            "attr": {
                                "name": "Повторность",
                                "attributeType": {
                                    "showLinkOnDocForm": True,
                                    "dictionary": True,
                                    "shortString": True
                                }
                            },
                            "value": "Повторное"
                        },
                    "inquiryReasonForReAppeal":
                        {
                            "attr": {
                                "name": "Причина повторного обращения",
                                "attributeType": {
                                    "name": "Справочник - Причина повторного обращения",
                                    "showLinkOnDocForm": True,
                                    "dictionary": True,
                                    "shortString": True,
                                }
                            },
                            "value": "Не согласен с решением местных органов"
                        },
                    "isPostSendingMethod":
                        {
                            "attr": {
                                "name": "Почтовое отправление",
                                "attributeType": {
                                    "name": "Логический boolean",
                                    "showLinkOnDocForm": True,
                                    "bool": True
                                }
                            },
                            "value": True
                        },
                    "isEmailSendingMethod":
                        {
                            "attr": {
                                "name": "Электронная почта",
                                "attributeType": {
                                    "name": "Логический boolean",
                                    "showLinkOnDocForm": True,
                                    "bool": True
                                }
                            },
                            "value": True
                        },
                    "isPersonalSendingMethod":
                        {
                            "attr": {
                                "name": "Выдача на руки",
                                "mnemonic": "isPersonalSendingMethod",
                                "attributeType": {
                                    "name": "Логический boolean",
                                    "showLinkOnDocForm": True,
                                    "bool": True
                                }
                            },
                            "value": True
                        }
                },
            "project": False,
            "deleted": False,
            "read": True,
            "hasRestrictions": True,
            "activeTab":
                {
                    "tabMnemonic": "inquiryTabDataCommon",
                    "force": False
                },
            "alternativeDocumentViewClass": None,
            "entityClass": "su.opencode.docflow.documents.domain.doc.DocumentEntity",
            "fullId": "8D0AF450-A68F-4944-BD3A-87D9B0623EB2_1DocumentEntity",
            "processParams":
                {
                    "processInstanceId": processInstanceId,
                    "connectionId": connectionIdWriting,
                    "historyId": historyId,
                    "variantName": "Зарегистрировать",
                    "votes": 1
                },
            "actionType": "APPLY"
        }
        return registration_body_put_part3

    def accept_for_execution_body(self, processInstanceId, historyId, connectionIdWriting, nextBlockId):
        accept_for_execution_body = {"attrValues": {},
                                     "project": False,
                                     "deleted": False,
                                     "read": True,
                                     "hasRestrictions": True,
                                     "activeTab": {
                                         "tabMnemonic": "execution_progress",
                                         "force": False
                                     },
                                     "alternativeDocumentViewClass": None,
                                     "entityClass": "su.opencode.docflow.documents.domain.doc.DocumentEntity",
                                     "processAwaiting": {
                                         "processInstanceId": f"{processInstanceId}",
                                         "formJs": None,
                                         "variants": [
                                             {
                                                 "variantName": "Принять к исполнению",
                                                 "variantCss": "navigation-btn-success",
                                                 "variantType": "MAIN",
                                                 "toastMessage": None,
                                                 "variantTooltip": None,
                                                 "closeType": "NO_VARIANTS",
                                                 "processInstanceId": f"{processInstanceId}",
                                                 "historyId": f"{historyId}",
                                                 "connectionId": f"{connectionIdWriting}",
                                                 "connectionTag": "accept_for_execution",
                                                 "nextBlockId": f"{nextBlockId}",
                                                 "viewOrder": 0,
                                                 "votes": 1,
                                                 "form": None,
                                                 "formParams": {}
                                             }
                                         ],
                                         "newRound": False,
                                         "errorMessage": None
                                     },
                                     "processParams": {
                                         "processInstanceId": f"{processInstanceId}",
                                         "connectionId": f"{connectionIdWriting}",
                                         "historyId": f"{historyId}",
                                         "variantName": "Принять к исполнению",
                                         "votes": 1
                                     },
                                     "actionType": "APPLY"
                                     }
        return accept_for_execution_body

    def execution_body(self, processInstanceId, historyId, connectionIdWriting, file_id):
        execution = {
            "attrValues":
                {
                    "inquiryClosureChecked":
                        {
                            "attr":
                                {
                                    "name": "Проверено",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "bool": True
                                        }
                                },
                            "value": True
                        },
                    "resultFilesList":
                        {
                            "attr":
                                {
                                    "name": "Файлы результата (список)",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "list": True
                                        }
                                },
                            "value":
                                [
                                    {
                                        "@rowId": None,
                                        "@removed": False,
                                        "@order": -1,
                                        "@modified": False,
                                        "resultFilesFile":
                                            {
                                                "id": file_id
                                            },
                                        "@resultFilesFile_text": "<Без имени>"
                                    }
                                ]
                        },
                    "executionConsiderationResult":
                        {
                            "attr":
                                {
                                    "name": "Результат рассмотрения",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "dictionary": True,
                                            "shortString": True
                                        }
                                },
                            "value": "Меры приняты"
                        },
                    "inquiryControlOffChecked":
                        {
                            "attr":
                                {
                                    "name": "Проверено",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "bool": True
                                        }
                                },
                            "value": True
                        }
                },
            "project": False,
            "deleted": False,
            "read": True,
            "hasRestrictions": True,
            "activeTab":
                {
                    "tabMnemonic": "execution_progress",
                    "force": False
                },
            "alternativeDocumentViewClass": None,
            "entityClass": "su.opencode.docflow.documents.domain.doc.DocumentEntity",
            "fullId": "8A61C546-CD16-454D-8047-6711D50AFC1E_1DocumentEntity",
            "processParams":
                {
                    "processInstanceId": f"{processInstanceId}",
                    "connectionId": f"{connectionIdWriting}",
                    "historyId": f"{historyId}",
                    "variantName": "Исполнено",
                    "votes": 1
                },
            "actionType": "SAVE"
        }
        return execution

    def body_agreement(self, processInstanceId, historyId, connectionIdWriting):
        body_agreement = {
            "attrValues":
                {},
            "project": False,
            "deleted": False,
            "read": True,
            "hasRestrictions": True,
            "activeTab":
                {
                    "tabMnemonic": "inquiryTabDataCommon",
                    "force": False
                },
            "alternativeDocumentViewClass": None,
            "entityClass": "su.opencode.docflow.documents.domain.doc.DocumentEntity",
            "fullId": "7417632B-6CE1-473B-992C-242CA081D192_5DocumentEntity",
            "processParams":
                {
                    "processInstanceId": processInstanceId,
                    "connectionId": connectionIdWriting,
                    "historyId": historyId,
                    "variantName": "Согласовать",
                    "votes": 1
                },
            "actionType": "APPLY"
        }
        return body_agreement

    def drop_control(self, processInstanceId, historyId, connectionIdWriting):
        drop_control = {
            "attrValues":
                {
                    "inquiryEmail":
                        {
                            "attr":
                                {
                                    "name": "Адрес электронной почты",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "shortString": True
                                        }
                                },
                            "value": "sdfdfs@mail.ru"
                        },
                    "withdrawFromControlPerson":
                        {
                            "attr":
                                {
                                    "name": "С контроля снял(а)",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "reference": True
                                        }
                                },
                            "value":
                                {
                                    "id": "871DB6A1-E1E6-47B1-9E4B-4509179319EF",
                                    "name": "Колесников Дмитрий Александрович - Инженер 2 категории",
                                    "entityClass": "su.opencode.docflow.auth.domain.DepartmentPosition",
                                    "formConfig":
                                        {
                                            "parentForm": "document-form-1291",
                                            "parentAttribute": "C699E73E-ABD3-4CF0-BAC4-A95F1180ACC0"
                                        }
                                }
                        },
                    "withdrawFromControlDate":
                        {
                            "attr":
                                {
                                    "name": "Дата снятия с контроля",
                                    "attributeType":
                                        {
                                            "showLink": True,
                                            "date": True
                                        }
                                },
                            "value": give_tomorrow_date()
                        }
                },
            "project": False,
            "deleted": False,
            "read": True,
            "hasRestrictions": True,
            "activeTab":
                {
                    "tabMnemonic": "inquiryTabDataCommon",
                    "force": False
                },
            "alternativeDocumentViewClass": None,
            "entityClass": "su.opencode.docflow.documents.domain.doc.DocumentEntity",
            "fullId": "2C98D40C-B3F6-4ABB-9BE3-BC58CFA9BDDF_9DocumentEntity",
            "processParams":
                {
                    "processInstanceId": processInstanceId,
                    "connectionId": connectionIdWriting,
                    "historyId": historyId,
                    "variantName": "Снять с контроля",
                    "votes": 1
                },
            "actionType": "APPLY"
        }
        return drop_control
