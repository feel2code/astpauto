#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext


# кнопка для скриптов да
def clicked():
    rz = txt.get()
    snils = txt2.get('1.0', '1.11')
    a1 = " select (select sc.cit_snils from msk.citizen as sc inner join msk.oper_history as so on sc.cit_id = so.cit_id inner join msk.portfolio as sp on so.oph_id = sp.oph_id inner join msk.doc as sd on sp.pf_id = sd.pf_id  where (sd.doc_id = d.doc_id)) as $$$_CLASSIC_$4_6388_8758208, d.doc_id, cdt.cdt_id, cdt.cdt_name, d.doc_incoming_num, d.doc_date, d.doc_is_actual, d.cou_code, d.pf_id, p.ccs_id, p.cou_code as expr1, de.dec_date,  de.dec_is_approve, de.dec_is_actual, de.dec_sum, de.app_id, cds.cds_name, a.app_sum, e.expt_short_name, d.doc_rec_date from msk.doc as d inner join msk.cls_doc_type as cdt on d.cdt_id = cdt.cdt_id inner join msk.portfolio as p on d.pf_id = p.pf_id left outer join msk.decision as de on de.doc_id = d.doc_id left outer join msk.cls_decision_status as cds on de.cds_id = cds.cds_id left outer join msk.application as a on d.doc_id = a.doc_id left outer join  msk.cls_expense_type as e on e.expt_id = a.expt_id where (d.pf_id in  (select p.pf_id from msk.portfolio as p inner join msk.oper_history as oh on p.oph_id = oh.oph_id inner join msk.citizen as c on oh.cit_id = c.cit_id where (c.cit_snils in (" + snils + ")))) and (((d.cdt_id < 92 or d.cdt_id > 288 or d.cdt_id in (97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 236, 237, 238, 254, 255, 258)) and d.cdt_id<1000) or ((d.cdt_id < 1092 or d.cdt_id > 1288 or d.cdt_id in (1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1236, 1237, 1238, 1254, 1255, 1258)) and d.cdt_id>1000)) order by $$$_CLASSIC_$4_6388_8758208, d.doc_date, d.doc_id;"
    a2 = "select msk.citizen_info.cinf_snils as $$$_APPLICATION_6388_8758208, a.* from msk.application as a inner join  msk.citizen_info on a.cinf_id = msk.citizen_info.per_id where (msk.citizen_info.cinf_snils = " + snils + ") and (a.doc_id is not null);"
    a3 = "select i.cinf_snils as $$$_DECISION_$_6388_8758208, msk.decision.* from msk.portfolio as p inner join msk.oper_history as o on p.oph_id = o.oph_id inner join  msk.citizen as c on o.cit_id = c.cit_id inner join msk.citizen_info as i on c.cinf_id = i.per_id inner join msk.doc as d on p.pf_id = d.pf_id inner join msk.decision on d.doc_id = msk.decision.doc_id where i.cinf_snils = " + snils + ";"
    a4 = "select cit.cit_snils as $$$_VYPISKA$_6388_8758208, op.opr_id, op.oph_id, op.doc_id, op.cot_id, op.opr_rec_date, op.opr_session_id, op.u_id, op.opr_sys_date, op.cause_doc_id, ot.cot_name, fop.opr_id as expr1, fop.fopr_sum, fop.fopr_available_sum, fop.fopr_reserved_sum, fop.fopr_remaining_sum, fop.cat_id from msk.operation as op inner join msk.cls_oper_type as ot on op.cot_id = ot.cot_id inner join msk.fin_operation as fop on op.opr_id = fop.opr_id inner join msk.oper_history as oph on op.oph_id = oph.oph_id inner join msk.citizen as cit on oph.cit_id = cit.cit_id where (cit.cit_snils = " + snils + ") order by op.opr_rec_date;"
    a5 = "select i.cinf_snils as $$$_PORTFOLIO_$_6388_8758208, p.pf_id, p.pf_num, p.cou_code, p.pf_law_id, p.pf_add_id, p.ccs_id, p.pf_creation_date, p.oph_id, p.pf_cou_code, p.pf_cou_name, p.cou_is_changed, p.is_deleted from msk.portfolio as p inner join msk.oper_history as o on p.oph_id = o.oph_id inner join msk.citizen as c on o.cit_id = c.cit_id inner join msk.citizen_info as i on c.cinf_id = i.per_id where (i.cinf_snils = " + snils + ") order by p.pf_id;"
    a6 = "select msk.citizen_info.cinf_snils as $$$_OPERATION_$_6388_8758208, msk.operation.opr_id, msk.operation.oph_id, msk.operation.doc_id, msk.operation.cot_id, msk.operation.opr_rec_date, msk.operation.opr_session_id, msk.operation.u_id, msk.operation.opr_sys_date, msk.operation.cause_doc_id from  msk.citizen inner join  msk.operation inner join  msk.oper_history on msk.operation.oph_id = msk.oper_history.oph_id on msk.citizen.cit_id = msk.oper_history.cit_id inner join  msk.citizen_info on msk.citizen.cinf_id = msk.citizen_info.per_id where (msk.citizen_info.cinf_snils = " + snils + ") order by msk.operation.opr_rec_date;"
    a7 = "select msk.citizen_info.cinf_snils as $$$_FIN_OPER_$_6388_8758208, msk.fin_operation.* from msk.citizen inner join msk.operation inner join  msk.oper_history on msk.operation.oph_id = msk.oper_history.oph_id on msk.citizen.cit_id = msk.oper_history.cit_id inner join msk.citizen_info on msk.citizen.cinf_id = msk.citizen_info.per_id inner join  msk.fin_operation on msk.operation.opr_id = msk.fin_operation.opr_id where msk.citizen_info.cinf_snils = " + snils + ";"
    a8 = "select i.cinf_snils as $$$_RECEIVER_$_6388_8758208, msk.receiver.* from msk.portfolio as p inner join msk.oper_history as o on p.oph_id = o.oph_id inner join msk.citizen as c on o.cit_id = c.cit_id inner join msk.citizen_info as i on c.cinf_id = i.per_id inner join  msk.doc as d on p.pf_id = d.pf_id inner join msk.payment on d.doc_id = msk.payment.doc_id inner join  msk.receiver on msk.payment.rec_id = msk.receiver.rec_id where (i.cinf_snils = " + snils + ");"
    a9 = "select msk.citizen_info.cinf_snils as $$$_CONTR_PAYM__6388_8758208, msk.contract_payment.* from msk.contract_payment inner join msk.application on msk.contract_payment.app_id = msk.application.doc_id inner join msk.citizen_info on msk.application.cinf_id = msk.citizen_info.per_id where (msk.citizen_info.cinf_snils = " + snils + ");"
    a10 = " select msk.citizen_info.cinf_snils as $$$_SUM_REQ$_6388_8758208, msk.summary_request.* from msk.contract_payment inner join msk.application on msk.contract_payment.app_id = msk.application.doc_id inner join msk.citizen_info on msk.application.cinf_id = msk.citizen_info.per_id inner join msk.summary_request_contract_payment on msk.contract_payment.cp_id = msk.summary_request_contract_payment.cp_id inner join msk.summary_request on msk.summary_request_contract_payment.sr_id = msk.summary_request.sr_id where (msk.citizen_info.cinf_snils = " + snils + ");"
    a11 = " SELECT MSK.CITIZEN_INFO.CINF_SNILS AS $$$_SUM_REQ_CON_6388_8758208, MSK.SUMMARY_REQUEST_CONTRACT_PAYMENT.SR_ID, MSK.SUMMARY_REQUEST_CONTRACT_PAYMENT.CP_ID FROM MSK.CONTRACT_PAYMENT INNER JOIN MSK.APPLICATION ON MSK.CONTRACT_PAYMENT.APP_ID = MSK.APPLICATION.DOC_ID INNER JOIN MSK.CITIZEN_INFO ON MSK.APPLICATION.CINF_ID = MSK.CITIZEN_INFO.PER_ID INNER JOIN MSK.SUMMARY_REQUEST_CONTRACT_PAYMENT ON MSK.CONTRACT_PAYMENT.CP_ID = MSK.SUMMARY_REQUEST_CONTRACT_PAYMENT.CP_ID WHERE        (MSK.CITIZEN_INFO.CINF_SNILS = " + snils + ");"
    a12 = "select msk.citizen_info.cinf_snils as $$$_SUM_CONT_PA_6388_8758208, msk.summary_contract_payment.psu_id, msk.summary_contract_payment.cp_id, msk.summary_contract_payment.cpse_id, msk.summary_contract_payment.scp_reason_comment, msk.summary_contract_payment.dec_id, msk.summary_contract_payment.original_cpse_id, msk.summary_contract_payment.dcr_id from msk.application as a inner join msk.citizen_info on a.cinf_id = msk.citizen_info.per_id inner join msk.contract_payment on a.doc_id = msk.contract_payment.app_id inner join msk.summary_contract_payment on msk.contract_payment.cp_id = msk.summary_contract_payment.cp_id where (msk.citizen_info.cinf_snils = " + snils + ");"
    a13 = "SELECT MSK.CITIZEN_INFO.CINF_SNILS AS $$$_REF_PAY_APP_6388_8758208, MSK.REFUND_PAY_APPENDIX.* FROM MSK.APPLICATION AS a INNER JOIN MSK.CITIZEN_INFO ON a.CINF_ID = MSK.CITIZEN_INFO.PER_ID INNER JOIN MSK.REFUND_PAY_APPENDIX ON a.DOC_ID = MSK.REFUND_PAY_APPENDIX.APP_ID WHERE (MSK.CITIZEN_INFO.CINF_SNILS = " + snils + ");"
    a14 = "select msk.citizen_info.cinf_snils as $$$_CALC_CONF_I_6388_8758208, msk.calc_confirm_info.* from msk.application as a inner join msk.citizen_info on a.cinf_id = msk.citizen_info.per_id inner join msk.calc_confirm_info on a.doc_id = msk.calc_confirm_info.doc_id where msk.citizen_info.cinf_snils = " + snils + ";"
    a15 = "select msk.citizen_info.cinf_snils as $$$_PAY_SUM$_6388_8758208, msk.payment_summary.psu_id, msk.payment_summary.psu_parent_id, msk.payment_summary.cou_code, msk.payment_summary.psu_approve_date, msk.payment_summary.psu_create_date, msk.payment_summary.psu_sum, msk.payment_summary.cst_id, msk.payment_summary.psu_is_approve, msk.payment_summary.psu_summary_date, msk.payment_summary.psu_count, msk.payment_summary.expd_id, msk.payment_summary.psu_from_date, msk.payment_summary.approve_user_id, msk.payment_summary.reg_approve_u_id, msk.payment_summary.create_user_id, msk.payment_summary.psu_cou_code, msk.payment_summary.psu_cou_name, msk.payment_summary.cou_is_changed, msk.payment_summary.psu_spu_send_date, msk.payment_summary.psu_spu_send_user_id from msk.application as a inner join msk.citizen_info on a.cinf_id = msk.citizen_info.per_id inner join msk.contract_payment on a.doc_id = msk.contract_payment.app_id inner join msk.summary_contract_payment on msk.contract_payment.cp_id = msk.summary_contract_payment.cp_id inner join msk.payment_summary on msk.summary_contract_payment.psu_id = msk.payment_summary.psu_id where (msk.citizen_info.cinf_snils = " + snils + ");"
    a16 = "select msk.citizen_info.cinf_snils as $$$_SUM_APP_BEN_6388_8758208, msk.summary_app_benefit.* from  msk.application as a inner join msk.citizen_info on a.cinf_id = msk.citizen_info.per_id inner join msk.summary_app_benefit on a.doc_id = msk.summary_app_benefit.doc_id where (msk.citizen_info.cinf_snils = " + snils + ");"
    a17 = "select i.cinf_snils as $$$_PAYSH_REG$_6388_8758208, msk.paysheet_register.* from msk.summary_contract_payment inner join msk.payment_summary on msk.summary_contract_payment.psu_id = msk.payment_summary.psu_id inner join msk.portfolio as p inner join msk.oper_history as o on p.oph_id = o.oph_id inner join msk.citizen as c on o.cit_id = c.cit_id inner join msk.citizen_info as i on c.cinf_id = i.per_id inner join msk.doc as d on p.pf_id = d.pf_id on msk.summary_contract_payment.dec_id = d.doc_id inner join msk.paysheet_register on msk.payment_summary.psu_id = msk.paysheet_register.psu_id where (i.cinf_snils = " + snils + ");"
    a18 = "select i.cinf_snils as $$$_PAYSHEET_$_6388_8758208, msk.paysheet.* from msk.portfolio as p inner join msk.oper_history as o on p.oph_id = o.oph_id inner join msk.citizen as c on o.cit_id = c.cit_id inner join msk.citizen_info as i on c.cinf_id = i.per_id inner join msk.doc as d on p.pf_id = d.pf_id inner join msk.payment on d.doc_id = msk.payment.doc_id inner join msk.paysheet on msk.payment.psh_id = msk.paysheet.psh_id where i.cinf_snils = " + snils + ";"
    a19 = "select i.cinf_snils as $$$_PAYSH_HIST$_6388_8758208, msk.paysheet_history.* from msk.portfolio as p inner join msk.oper_history as o on p.oph_id = o.oph_id inner join msk.citizen as c on o.cit_id = c.cit_id inner join msk.citizen_info as i on c.cinf_id = i.per_id inner join msk.doc as d on p.pf_id = d.pf_id inner join msk.payment on d.doc_id = msk.payment.doc_id inner join msk.paysheet on msk.payment.psh_id = msk.paysheet.psh_id inner join msk.paysheet_history on msk.paysheet.psh_id = msk.paysheet_history.psh_id where (i.cinf_snils = " + snils + ");"
    a20 = "SELECT MSK.CITIZEN_INFO.CINF_SNILS AS $$$_CONTRACT$_6388_8758208, MSK.CONTRACT.CT_ID, MSK.CONTRACT.CT_NUM, MSK.CONTRACT.CT_SUM, MSK.CONTRACT.CT_FIO, MSK.CONTRACT.CT_RECIPIENT_COUNT, MSK.CONTRACT.CT_BILL_NUM,  MSK.CONTRACT.CT_LOAN_NUM, MSK.CONTRACT.APP_ID, MSK.CONTRACT.CT_DATE, MSK.CONTRACT.CT_NOTE FROM MSK.APPLICATION AS a INNER JOIN MSK.CITIZEN_INFO ON a.CINF_ID = MSK.CITIZEN_INFO.PER_ID INNER JOIN MSK.CONTRACT ON a.DOC_ID = MSK.CONTRACT.APP_ID WHERE (MSK.CITIZEN_INFO.CINF_SNILS = " + snils + ");"
    a21 = "select i.cinf_snils as $$$_PAYMENT_$_6388_8758208, msk.payment.* from msk.portfolio as p inner join  msk.oper_history as o on p.oph_id = o.oph_id inner join  msk.citizen as c on o.cit_id = c.cit_id inner join msk.citizen_info as i on c.cinf_id = i.per_id inner join  msk.doc as d on p.pf_id = d.pf_id inner join msk.payment on d.doc_id = msk.payment.doc_id where (i.cinf_snils = " + snils + ");"
    a22 = "select i.cinf_snils as $$$_PAY_CON_PAY_6388_8758208, msk.payment_contract_payment.cp_id, msk.payment_contract_payment.pay_id from msk.portfolio as p inner join msk.oper_history as o on p.oph_id = o.oph_id inner join msk.citizen as c on o.cit_id = c.cit_id inner join msk.citizen_info as i on c.cinf_id = i.per_id inner join msk.doc as d on p.pf_id = d.pf_id inner join  msk.payment on d.doc_id = msk.payment.doc_id inner join  msk.payment_contract_payment on msk.payment.doc_id = msk.payment_contract_payment.pay_id where (i.cinf_snils = " + snils + ");"
    a23 = "select i.cinf_snils as $$$_PERSON_$_6388_8758208, p.per_id, p.per_lastname, p.per_patronymic, p.per_name, p.per_birth_date, p.per_birth_place, p.ctz_id, p.per_country_code, p.per_gender, p.per_birth_year, p.per_birth_month, p.per_birth_day, p.dat_id from msk.person p inner join  msk.citizen_info i on p.per_id = i.per_id where  i.cinf_snils = " + snils + ";"
    a24 = "SELECT i.CINF_SNILS AS $$$_PAYSH_PAYSH_6388_8758208, MSK.PAYSHEET.*, MSK.PAYSHEET_CONTRACT_PAYMENT.CP_ID, MSK.PAYSHEET_CONTRACT_PAYMENT.PCP_SUM,  MSK.PAYSHEET_CONTRACT_PAYMENT.PCP_INDEX_NUM, MSK.PAYSHEET_CONTRACT_PAYMENT.DCR_ID, MSK.PAYMENT.DOC_ID, MSK.PAYMENT.PAY_SUM, MSK.PAYMENT.PAY_TYPE, MSK.PAYMENT.APP_ID,  MSK.PAYMENT.DEC_ID, MSK.PAYMENT.REC_ID FROM MSK.PORTFOLIO AS p INNER JOIN MSK.OPER_HISTORY AS o ON p.OPH_ID = o.OPH_ID INNER JOIN MSK.CITIZEN AS c ON o.CIT_ID = c.CIT_ID INNER JOIN MSK.CITIZEN_INFO AS i ON c.CINF_ID = i.PER_ID INNER JOIN MSK.DOC AS d ON p.PF_ID = d.PF_ID INNER JOIN MSK.PAYMENT ON d.DOC_ID = MSK.PAYMENT.DOC_ID INNER JOIN MSK.PAYSHEET ON MSK.PAYMENT.PSH_ID = MSK.PAYSHEET.PSH_ID INNER JOIN MSK.PAYSHEET_CONTRACT_PAYMENT ON MSK.PAYSHEET.PSH_ID = MSK.PAYSHEET_CONTRACT_PAYMENT.PSH_ID WHERE (i.CINF_SNILS =" + snils + ");"
    a25 = "select msk.citizen_info.cinf_snils as $$$_PAYSH_CONTR_6388_8758208, msk.paysheet_contract_payment.psh_id, msk.paysheet_contract_payment.cp_id, msk.paysheet_contract_payment.pcp_sum, msk.paysheet_contract_payment.pcp_index_num, msk.paysheet_contract_payment.dcr_id from msk.contract_payment inner join msk.application on msk.contract_payment.app_id = msk.application.doc_id inner join msk.citizen_info on msk.application.cinf_id = msk.citizen_info.per_id inner join msk.paysheet_contract_payment on msk.contract_payment.cp_id = msk.paysheet_contract_payment.cp_id where (msk.citizen_info.cinf_snils = " + snils + ");"
    a26 = "select i.cinf_snils as $$$_CHANGE_REQ$_6388_8758208, msk.change_requisites.dcr_id, msk.change_requisites.dcr_rs, msk.change_requisites.dcr_bank, msk.change_requisites.dcr_bik, msk.change_requisites.dcr_inn, msk.change_requisites.dcr_kpp, msk.change_requisites.dcr_ks, msk.change_requisites.dcr_fio, msk.change_requisites.cib_id, msk.change_requisites.refund_pay_id, msk.change_requisites.transfer_pay_id, msk.change_requisites.dcr_kbk, msk.change_requisites.dcr_oktmo from msk.portfolio as p inner join msk.oper_history as o on p.oph_id = o.oph_id inner join msk.citizen as c on o.cit_id = c.cit_id inner join msk.citizen_info as i on c.cinf_id = i.per_id inner join msk.doc as d on p.pf_id = d.pf_id inner join msk.payment on d.doc_id = msk.payment.doc_id inner join msk.receiver on msk.payment.rec_id = msk.receiver.rec_id inner join msk.change_requisites on msk.receiver.rec_id = msk.change_requisites.rec_id where (i.cinf_snils = " + snils + ");"
    a27 = "SELECT i.CINF_SNILS AS $$$_CHANGE_REQ1_6388_8758208, MSK.CHANGE_REQUISITES.DCR_ID, MSK.CHANGE_REQUISITES.DCR_RS, MSK.CHANGE_REQUISITES.DCR_BANK, MSK.CHANGE_REQUISITES.DCR_BIK,  MSK.CHANGE_REQUISITES.DCR_INN, MSK.CHANGE_REQUISITES.DCR_KPP, MSK.CHANGE_REQUISITES.DCR_KS, MSK.CHANGE_REQUISITES.DCR_FIO, MSK.CHANGE_REQUISITES.CIB_ID,  MSK.CHANGE_REQUISITES.REFUND_PAY_ID, MSK.CHANGE_REQUISITES.TRANSFER_PAY_ID, MSK.CHANGE_REQUISITES.DCR_KBK, MSK.CHANGE_REQUISITES.DCR_OKTMO, MSK.CHANGE_REQUISITES.REC_ID FROM MSK.PORTFOLIO AS p INNER JOIN MSK.OPER_HISTORY AS o ON p.OPH_ID = o.OPH_ID INNER JOIN MSK.CITIZEN AS c ON o.CIT_ID = c.CIT_ID INNER JOIN MSK.CITIZEN_INFO AS i ON c.CINF_ID = i.PER_ID INNER JOIN MSK.DOC AS d ON p.PF_ID = d.PF_ID INNER JOIN MSK.CHANGE_REQUISITES ON d.DOC_ID = MSK.CHANGE_REQUISITES.DCR_ID WHERE        (i.CINF_SNILS = " + snils + ");"
    a28 = "SELECT i.CINF_SNILS AS $$$_PAYM_SUM_P__6388_8758208, MSK.PAYMENT_SUMMARY.PSU_ID, MSK.PAYMENT_SUMMARY_DOC.DOC_ID AS P_S_D_DOC_ID, d.DOC_DATE, MSK.PAYMENT_SUMMARY_DOC.CPSE_ID AS P_S_D_CPSE_ID,  MSK.PAYMENT_SUMMARY.PSU_PARENT_ID, MSK.PAYMENT_SUMMARY.COU_CODE, MSK.PAYMENT_SUMMARY.PSU_APPROVE_DATE, MSK.PAYMENT_SUMMARY.PSU_CREATE_DATE,  MSK.PAYMENT_SUMMARY.PSU_SUM, MSK.PAYMENT_SUMMARY.CST_ID, MSK.PAYMENT_SUMMARY.PSU_IS_APPROVE, MSK.PAYMENT_SUMMARY.PSU_SUMMARY_DATE, MSK.PAYMENT_SUMMARY.PSU_COUNT,  MSK.PAYMENT_SUMMARY.EXPD_ID, MSK.PAYMENT_SUMMARY.PSU_FROM_DATE, MSK.PAYMENT_SUMMARY.APPROVE_USER_ID, MSK.PAYMENT_SUMMARY.REG_APPROVE_U_ID,  MSK.PAYMENT_SUMMARY.CREATE_USER_ID, MSK.PAYMENT_SUMMARY.PSU_COU_CODE, MSK.PAYMENT_SUMMARY.PSU_COU_NAME, MSK.PAYMENT_SUMMARY.COU_IS_CHANGED,  MSK.PAYMENT_SUMMARY.PSU_SPU_SEND_DATE, MSK.PAYMENT_SUMMARY.PSU_SPU_SEND_USER_ID FROM MSK.PORTFOLIO AS p INNER JOIN MSK.OPER_HISTORY AS o ON p.OPH_ID = o.OPH_ID INNER JOIN MSK.CITIZEN AS c ON o.CIT_ID = c.CIT_ID INNER JOIN MSK.CITIZEN_INFO AS i ON c.CINF_ID = i.PER_ID INNER JOIN MSK.DOC AS d ON p.PF_ID = d.PF_ID INNER JOIN MSK.PAYMENT_SUMMARY_DOC ON d.DOC_ID = MSK.PAYMENT_SUMMARY_DOC.DOC_ID INNER JOIN MSK.PAYMENT_SUMMARY ON MSK.PAYMENT_SUMMARY_DOC.PSU_ID = MSK.PAYMENT_SUMMARY.PSU_ID WHERE        (i.CINF_SNILS = " + snils + ") ORDER BY d.DOC_DATE;"
    script = (
                a1 + " " + a2 + " " + a3 + " " + a4 + " " + a5 + " " + a6 + " " + a7 + " " + a8 + " " + a9 + " " + a10 + " " + a11 + " " + a12 + " " + a13 + " " + a14 + " " + a15 + " " + a16 + " " + a17 + " " + a18 + " " + a19 + " " + a20 + " " + a21 + " " + a22 + " " + a23 + " " + a24 + " " + a25 + " " + a26 + " " + a27 + " " + a28)
    pyperclip.copy(script)
    driver = webdriver.Firefox(executable_path='/Users/felixmac/PycharmProjects/pythonProject/geckodriver')
    driver.get('http://astp/maximo/')
    s_username = driver.find_element_by_name("username")
    s_password = driver.find_element_by_name('password')
    s_username.send_keys("ivanovaeln")
    s_password.send_keys("Eivan9073-")
    driver.find_element_by_class_name('tiv_btn').click()
    time.sleep(1)
    driver.find_element_by_class_name('homebutton').click()
    time.sleep(3)
    driver.find_element_by_id('m1e20cba1-sct_42772').click()
    time.sleep(2)
    driver.find_element_by_id('me148583e-hb_header_10').click()
    time.sleep(12)
    driver.find_element_by_id('quicksearch').click()
    driver.find_element_by_id('quicksearch').send_keys(rz)
    driver.find_element_by_id('quicksearch').send_keys(Keys.RETURN)
    time.sleep(8)
    driver.find_element_by_id('m3b854f9f-sc_div').click()
    time.sleep(8)
    driver.find_element_by_id('ma7efa7a3-tb').click()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('Выполнить селект')
    driver.find_element_by_id('m6bda82c1-ta').click()
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    driver.find_element_by_id('m9e96a86b-tb').click()
    driver.find_element_by_id('m9e96a86b-tb').send_keys('25. \ 25.2. \ 25.2.2.')
    driver.find_element_by_id('m1317c3f5-pb').click()
    time.sleep(90)
    driver.find_element_by_id('m15f1c9f0-pb').click()
    driver.quit()
    txt2.delete('1.0', tk.END)
    i = 0
    while i < 35:
        txt.delete(0)
        i += 1


# кнопка для выборки
def clickedvib():
    rz = txt.get()
    script = txt2.get('1.0', tk.END)
    pyperclip.copy(script)
    driver = webdriver.Firefox(executable_path='/Users/felixmac/PycharmProjects/pythonProject/geckodriver')
    driver.get('http://astp/maximo/')
    s_username = driver.find_element_by_name("username")
    s_password = driver.find_element_by_name('password')
    s_username.send_keys("ivanovaeln")
    s_password.send_keys("Eivan9073-")
    driver.find_element_by_class_name('tiv_btn').click()
    time.sleep(1)
    driver.find_element_by_class_name('homebutton').click()
    time.sleep(3)
    driver.find_element_by_id('m1e20cba1-sct_42772').click()
    time.sleep(2)
    driver.find_element_by_id('me148583e-hb_header_10').click()
    time.sleep(12)
    driver.find_element_by_id('quicksearch').click()
    driver.find_element_by_id('quicksearch').send_keys(rz)
    driver.find_element_by_id('quicksearch').send_keys(Keys.RETURN)
    time.sleep(8)
    driver.find_element_by_id('m3b854f9f-sc_div').click()
    time.sleep(8)
    driver.find_element_by_id('ma7efa7a3-tb').click()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('Приложить выборку')
    driver.find_element_by_id('m6bda82c1-ta').click()
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    driver.find_element_by_id('m9e96a86b-tb').click()
    driver.find_element_by_id('m9e96a86b-tb').send_keys('25. \ 25.2. \ 25.2.2.')
    driver.find_element_by_id('m1317c3f5-pb').click()
    time.sleep(90)
    driver.find_element_by_id('m15f1c9f0-pb').click()
    driver.quit()
    txt2.delete('1.0', tk.END)
    i = 0
    while i < 35:
        txt.delete(0)
        i += 1


# кнопка ручного селекта
def clickedmanual():
    rz = txt.get()
    script = txt2.get('1.0', tk.END)
    pyperclip.copy(script)
    driver = webdriver.Firefox(executable_path='/Users/felixmac/PycharmProjects/pythonProject/geckodriver')
    driver.get('http://astp/maximo/')
    s_username = driver.find_element_by_name("username")
    s_password = driver.find_element_by_name('password')
    s_username.send_keys("ivanovaeln")
    s_password.send_keys("Eivan9073-")
    driver.find_element_by_class_name('tiv_btn').click()
    time.sleep(1)
    driver.find_element_by_class_name('homebutton').click()
    time.sleep(3)
    driver.find_element_by_id('m1e20cba1-sct_42772').click()
    time.sleep(2)
    driver.find_element_by_id('me148583e-hb_header_10').click()
    time.sleep(12)
    driver.find_element_by_id('quicksearch').click()
    driver.find_element_by_id('quicksearch').send_keys(rz)
    driver.find_element_by_id('quicksearch').send_keys(Keys.RETURN)
    time.sleep(8)
    driver.find_element_by_id('m3b854f9f-sc_div').click()
    time.sleep(8)
    driver.find_element_by_id('ma7efa7a3-tb').click()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('Выполнить селект')
    driver.find_element_by_id('m6bda82c1-ta').click()
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    driver.find_element_by_id('m9e96a86b-tb').click()
    driver.find_element_by_id('m9e96a86b-tb').send_keys('25. \ 25.2. \ 25.2.2.')
    driver.find_element_by_id('m1317c3f5-pb').click()
    time.sleep(90)
    driver.find_element_by_id('m15f1c9f0-pb').click()
    driver.quit()
    txt2.delete('1.0', tk.END)
    i = 0
    while i < 35:
        txt.delete(0)
        i += 1


# кнопка апдейта
def clickedupdate():
    rz = txt.get()
    script = txt2.get('1.0', tk.END)
    pyperclip.copy(script)
    driver = webdriver.Firefox(executable_path='/Users/felixmac/PycharmProjects/pythonProject/geckodriver')
    driver.get('http://astp/maximo/')
    s_username = driver.find_element_by_name("username")
    s_password = driver.find_element_by_name('password')
    s_username.send_keys("ivanovaeln")
    s_password.send_keys("Eivan9073-")
    driver.find_element_by_class_name('tiv_btn').click()
    time.sleep(1)
    driver.find_element_by_class_name('homebutton').click()
    time.sleep(3)
    driver.find_element_by_id('m1e20cba1-sct_42772').click()
    time.sleep(2)
    driver.find_element_by_id('me148583e-hb_header_10').click()
    time.sleep(12)
    driver.find_element_by_id('quicksearch').click()
    driver.find_element_by_id('quicksearch').send_keys(rz)
    driver.find_element_by_id('quicksearch').send_keys(Keys.RETURN)
    time.sleep(8)
    driver.find_element_by_id('m3b854f9f-sc_div').click()
    time.sleep(8)
    driver.find_element_by_id('ma7efa7a3-tb').click()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('Просьба согласовать выполнение скриптов')
    driver.find_element_by_id('m6bda82c1-ta').click()
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    driver.find_element_by_id('m9e96a86b-tb').click()
    driver.find_element_by_id('m9e96a86b-tb').send_keys('25. \ 25.7.')
    driver.find_element_by_id('m1317c3f5-pb').click()
    time.sleep(90)
    driver.find_element_by_id('m15f1c9f0-pb').click()
    driver.quit()
    txt2.delete('1.0', tk.END)
    i = 0
    while i < 35:
        txt.delete(0)
        i += 1
# настройка окна
window = Tk()
top = Frame(window)
bottom = Frame(window)
window.title('Выгрузка данных по СНИЛСУ в АСТП')
window.geometry('550x300')
txt = Entry(top, width=19)
txt2 = scrolledtext.ScrolledText(bottom, width=70, height=20)
btn1 = Button(top, text="Выборка", command=clickedvib)
btn = Button(top, text="Скрипты", command=clicked)
btn2 = Button(top, text="Ручной селект", command=clickedmanual)
btn3 = Button(top, text="Ручной апдейт", command=clickedupdate)
top.pack()
bottom.pack()
txt.pack(side=LEFT)
btn1.pack(side=LEFT)
btn.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
txt2.pack(side=LEFT)
window.mainloop()
