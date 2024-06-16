import os
from datetime import date

from langchain_core.tools import tool

import requests
from dotenv import load_dotenv
load_dotenv()
domain = os.environ['API_DOMAIN']
token = os.environ['TEAM_TOKEN']

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}

@tool
def get_company_info(company_name: str):
  '''根据公司名称获得该公司所有基本信息'''
  url = f"https://{domain}/law_api/get_company_info"
  data = {
    "company_name": company_name
  }
  
  rsp = requests.post(url, json=data, headers=headers)
  return rsp.json()

@tool
def search_company_name_by_info(key: str, value: str):
  '''根据公司基本信息，查询具体的公司名称
  '''
  url = f"https://{domain}/law_api/search_company_name_by_info"
  data = {
    "key": key,
    "value": value,
  }
  
  rsp = requests.post(url, json=data, headers=headers)
  return rsp.json()


@tool
def get_company_register(company_name: str):
  '''根据公司名称获得该公司所有注册信息'''
  url = f"https://{domain}/law_api/get_company_register"
  data = {
    "company_name": company_name
  }
  
  rsp = requests.post(url, json=data, headers=headers)
  return rsp.json()


@tool
def search_company_name_by_register(key: str, value: str):
  '''根据公司注册信息，查询具体的公司名称
     示例：根据注册号查找公司名称. key: 注册号, value: 320512400000458
  '''
  url = f"https://{domain}/law_api/search_company_name_by_register"
  data = {
    "key": key,
    "value": value,
  }
  
  rsp = requests.post(url, json=data, headers=headers)
  return rsp.json()


@tool
def get_sub_company_info(company_name: str):
  '''根据公司名称获得该公司所有关联子公司信息'''
  url = f"https://{domain}/law_api/get_sub_company_info"
  data = {
    "company_name": company_name
  }
  
  rsp = requests.post(url, json=data, headers=headers)
  return rsp.json()


@tool
def search_company_name_by_sub_info(key: str, value: str):
  '''根据关联子公司信息某个字段是某个值来查询具体的公司名称'''
  url = f"https://{domain}/law_api/search_company_name_by_sub_info"
  data = {
    "key": key,
    "value": value,
  }
  
  rsp = requests.post(url, json=data, headers=headers)
  return rsp.json()


@tool
def get_legal_document(case_num: str):
  '''根据案号获得该案所有基本信息'''
  url = f"https://{domain}/law_api/get_legal_document"
  data = {
    "case_num": case_num
  }
  
  rsp = requests.post(url, json=data, headers=headers)
  return rsp.json()


@tool
def search_case_num_by_legal_document(key: str, value: str):
  '''根据法律文书某个字段是某个值来查询具体的案号'''
  url = f"https://{domain}/law_api/search_case_num_by_legal_document"
  data = {
    "key": key,
    "value": value,
  }

  rsp = requests.post(url, json=data, headers=headers)
  return rsp.json()

# @tool
# def current_date() -> date:
#   """get the current date"""
#   today = date.today()
#   return today
