AUTH_PAGE_URL = '/MinsoprDocflow/'
WORK_URL = f'{AUTH_PAGE_URL}minsopr/'
DOCUMENT_DO_URL = f'{WORK_URL}index.do'
LOGOUT_URL = f'{WORK_URL}logout.do'
OPEN_APPEALS_LIST_URL = f'{WORK_URL}navigator/inquiry/grid.json?_dc=1654007189600&docTypeId=A616637B' \
                        '-D7F6-4C20-A978-69D65C0AD4DC&navigatorNodeType=ALL_INQUIRIES&inquiryStatusId=&initGrid=True' \
                        '&paging=True&unreadFirst=False&expireFilter=NONE&page=1&start=0&limit=50'
DOCFLOW = '/MinsoprDocflow/docflow/'
EDITOR_URL = f'{DOCFLOW}editor/'
STORAGE_URL = f'{DOCFLOW}storage/multiUpload?'
CREATE_APPEAL_FORM_URL = f'{EDITOR_URL}document/?docTypeId=A616637B-D7F6-4C20-A978-69D65C0AD4DC'
ATTR_VALUE = f'{EDITOR_URL}attr-values/?docTypeId=A616637B-D7F6-4C20-A978-69D65C0AD4DC'
DOCFLOW_DOCUMENTS_URL = f'{AUTH_PAGE_URL}docflow/document/'


def appeal_doc_id_url(doc_id):
    return f'{DOCFLOW_DOCUMENTS_URL}{doc_id}?&meta=True'


# def attr_value(attribute_name):
#     return f'{EDITOR_URL}attr-values/?&attribute={attribute_name}&documentTypeId=A616637B-D7F6-4C20-A978-69D65C0AD4DC'

def attr_value(attribute_name):
    return f'{EDITOR_URL}attr-values/?&attribute={attribute_name}&documentTypeId=A616637B-D7F6-4C20-A978-69D65C0AD4DC'


def registration_appeal_write_url(doc_id):
    return f"/MinsoprDocflow/docflow/editor/document/{doc_id}"


def appeal_res_url(doc_id):
    return f'{DOCFLOW_DOCUMENTS_URL}{doc_id}?&meta=True&group=DOC'


def get_isp_id(doc_id):
    return f'{WORK_URL}common/inquiries/content-tree?_dc=1661175019939&id={doc_id}&node=root'


def get_sogl(doc_id):
    return f'/MinsoprDocflow/docflow/document/{doc_id}?_dc=1661339550995&meta=true&group=DOC'
