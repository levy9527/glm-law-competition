from langchain_core.tools import tool
import api

@tool
def get_company_info(company_name: str):
  '''根据公司名称获得该公司所有基本信息'''
  return api.get_company_info(company_name)


@tool
def search_company_name_by_info(key: str, value: str):
  '''根据公司基本信息，返回公司名称列表
  '''
  return api.search_company_name_by_info(key, value)


@tool
def get_company_register(company_name: str):
  '''根据公司名称获得该公司所有注册信息'''
  return api.get_company_register(company_name)


@tool
def search_company_name_by_register(key: str, value: str):
  '''根据公司注册信息，查询具体的公司名称
     示例：根据注册号查找公司名称. key: 注册号, value: 320512400000458
  '''
  return api.search_company_name_by_register(key, value)


@tool
def get_sub_company_info(company_name: str):
  '''根据公司名称获得该公司所有关联子公司信息'''
  return api.get_sub_company_info(company_name)


@tool
def search_company_name_by_sub_info(key: str, value: str):
  '''根据关联子公司信息某个字段是某个值来查询具体的公司名称'''
  return api.search_company_name_by_sub_info(key, value)


@tool
def get_legal_document(case_num: str):
  '''根据案号获得该案所有基本信息'''
  return api.get_legal_document(case_num)


@tool
def search_case_num_by_legal_document(key: str, value: str):
  '''根据法律文书某个字段是某个值来查询具体的案号'''
  return api.search_case_num_by_legal_document(key, value)


# 组合性的问题，可以通过prompt指示，让大模型去调用，也可以自己写代码。后者更稳定
@tool
def list_company_register_by_industry(industry: str):
  '''根据行业名称，返回该行业的所有公司的注册信息
     industry 示例：批发业
  '''
  return api.list_company_register_by_industry(industry)

# @tool
# def current_date() -> date:
#   """get the current date"""
#   today = date.today()
#   return today
