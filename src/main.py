from typing import Any

from src.get_data import reading_csv, reading_excel
from src.process_bank import process_bank_search
from src.processing import filter_by_currensy, filter_by_currensy_json, filter_by_state, sort_by_date
from src.utils import reading_json
from src.widget import get_date, mask_account_card

wellcome_str = "Программа: Привет! Добро пожаловать в программу работы \nс банковскими транзакциями. \nВыберите необходимый пункт меню:"

question_ = [
    "1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла\n",
    "Введите статус, по которому необходимо выполнить фильтрацию. \nДоступные для фильтровки статусы: EXECUTED(1), CANCELED(2), PENDING(3)\n",
    "Отсортировать операции по дате? Да(1)/Нет(2)\n",
    "Отсортировать по возрастанию(1) или по убыванию(2)?\n",
    "Выводить только рублевые транзакции? Да(1)/Нет(2)\n",
    "Отфильтровать список транзакций по определенному слову \nв описании? Да(1)/Нет(2)\n",
]
acsept_ans = [["1", "2", "3"], ["1", "2", "3"], ["1", "2"], ["1", "2"], ["1", "2"], ["1", "2"]]
acsept_ans_ = [
    ["JSON", "CSV", "EXCEL"],
    ["EXECUTED", "CANCELED", "PENDING"],
    ["ДА", "НЕТ"],
    ["ВОЗРАСТАНИЮ", "УБЫВАНИЮ"],
    ["ДА", "НЕТ"],
    ["ДА", "НЕТ"],
]
pr_response = ["Для обработки выбран файл", "Операции отфильтрованы по статусу"]
wrong_ans_status = "Статус операции недоступен"

print_message = "Распечатываю итоговый список транзакций...\nВсего банковских операций в выборке:"
nothing_message="Не найдено ни одной транзакции, подходящей под ваши\nусловия фильтрации"
address_str = [
    "C:/Users/Admin/PycharmProjects/PythonProject1/data/operations.json",
    "C:/Users/Admin/PycharmProjects/PythonProject1/data/transactions.csv",
    "C:/Users/Admin/PycharmProjects/PythonProject1/data/transactions_excel.xlsx",
]

user_responce = ["", "", "", "", "", ""]


def main() -> None:
    print(wellcome_str)
    user_responce[0] = dialog(question_[0], acsept_ans[0], acsept_ans_[0], info=pr_response[0])
    user_responce[1] = dialog(question_[1], acsept_ans[1], acsept_ans_[1], wrong_ans_status, pr_response[1])
    user_responce[2] = dialog(question_[2], acsept_ans[2], acsept_ans_[2])
    if user_responce[2] == "1":
        user_responce[3] = dialog(question_[3], acsept_ans[3], acsept_ans_[3])
    user_responce[4] = dialog(question_[4], acsept_ans[4], acsept_ans_[4])
    user_responce[5] = dialog(question_[5], acsept_ans[5], acsept_ans_[5])

    working_dictionary = []
    if user_responce[0] == "1":
        working_dictionary = reading_json(address_str[0])
    if user_responce[0] == "2":
        working_dictionary = reading_csv(address_str[1])
    if user_responce[0] == "3":
        working_dictionary = reading_excel(address_str[2])
    if user_responce[1] == "1":
        working_dictionary = filter_by_state(working_dictionary)
    if user_responce[1] == "2":
        working_dictionary = filter_by_state(working_dictionary, "CANCELED")
    if user_responce[1] == "3":
        working_dictionary = filter_by_state(working_dictionary, "PENDING")
    if user_responce[2] == "1":
        if user_responce[3] == "1":
            working_dictionary = sort_by_date(working_dictionary)
        if user_responce[3] == "2":
            working_dictionary = sort_by_date(working_dictionary, sort_order=False)
    if user_responce[4] == "1":
        if user_responce[0] == "1":
            working_dictionary = filter_by_currensy_json(working_dictionary)
        if user_responce[0] != "1":
            working_dictionary = filter_by_currensy(working_dictionary)
    if user_responce[5] == "1":
        filter_info = input("По какому слову фильтровать?")
        working_dictionary = process_bank_search(working_dictionary, filter_info)
    if len(working_dictionary) == 0:
        print(nothing_message)
    else:
        print(print_message, len(working_dictionary))

        for i in working_dictionary:
            print()
            print(get_date(i["date"]), i["description"])
            if i.get("from"):
                print(mask_account_card(i["from"]), "->", mask_account_card(i["to"]))
            else:
                print(mask_account_card(i["to"]))
            if user_responce[0] == "1":
                print("Сумма:", i["operationAmount"]["amount"], i["operationAmount"]["currency"]["code"])
            else:
                print("Сумма:", i["amount"], i["currency_code"])


def dialog(promt_: str, short_ans: Any, long_ans: Any, wrong_ans: str = "невозможный ответ", info: str = "") -> str:
    while True:
        input_ = input(promt_).upper()
        if short_ans.count(input_) + long_ans.count(input_) >= 1:
            break
        else:
            print(wrong_ans)
    if info:
        if long_ans.count(input_) >= 1:
            print(info, input_)
        else:
            print(info, long_ans[int(input_) - 1])

    if long_ans.count(input_) >= 1:
        input_ = str(short_ans[long_ans.index(input_)])

    return input_


main()
