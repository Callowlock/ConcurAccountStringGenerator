from app.utils import (
    parse_input,
    require_non_empty,
    validate_equal_lengths,
    validate_delete_flags,
    validate_departments,
    parse_input_allow_empty,
)

import pandas as pd


def generate_xlsx(
    dept_str,
    store_str,
    fname_str,
    minit_required,
    minit_str,
    lname_str,
    thirdE_str,
    delete_str,
):

    print(minit_required)
    dictionary = {
        "Moonbase Ops": ["82011", "82013", "82021", "82101", "82888", "82014"],
        "Galactic Wellness & Training": [
            "87101",
            "87011",
            "87013",
            "87014",
            "87021",
            "87041",
        ],
        "Command Deck": ["81013", "81011", "81014"],
        "Habitat Systems": ["85141", "85143", "85144", "85151"],
        "Data Processing Core": ["84011", "84013", "84014", "84021", "84041", "84101"],
        "Supply Bay": [
            "92013",
            "92014",
            "92011",
            "92021",
            "92177",
            "92288",
            "92777",
            "23603",
        ],
        "Quantum Prime": [
            "91013",
            "91011",
            "91021",
            "91177",
            "91288",
            "91014",
            "91777",
        ],
        "Repair Division": [
            "93013",
            "93011",
            "93017",
            "93021",
            "93177",
            "93288",
            "93399",
            "23603",
            "93014",
        ],
        "Ledger & Council": [
            "93052",
            "93053",
            "93080",
            "93120",
            "WarpTravel",
            "93050",
            "93060",
        ],
    }

    dept_index_map = {
        "0": "Moonbase Ops",
        "1": "Galactic Wellness & Training",
        "2": "Command Deck",
        "3": "Habitat Systems",
        "4": "Data Processing Core",
        "5": "Supply Bay",
        "6": "Quantum Prime",
        "7": "Repair Division",
        "8": "Ledger & Council",
    }

    # --- Department mapping and validation ---
    dept_input_raw = parse_input(dept_str)
    dept_input_list = list(map(dept_index_map.get, dept_input_raw))
    require_non_empty(dept_input_list, "Department(s)")

    # Check for values not in range 0-7
    validate_departments(dept_input_raw, dept_input_list)

    # --- Input validation and parsing ---
    store_list = require_non_empty(parse_input(store_str), "Sector #'s")
    fname_list = require_non_empty(parse_input(fname_str), "First Name(s)")
    lname_list = require_non_empty(parse_input(lname_str), "Last Name(s)")

    print(store_list, fname_list, lname_list)

    thirdE_list = require_non_empty(
        parse_input(thirdE_str, to_upper=True), "Third Element(s)"
    )
    delete_list = require_non_empty(
        parse_input(delete_str, to_upper=True), "Delete Flag(s)"
    )

    # --- Middle Initial ---
    if minit_required == "Y":
        minit_list = require_non_empty(
            parse_input_allow_empty(minit_str, to_upper=True), "Middle Initial(s)"
        )
    else:
        minit_list = [""] * len(fname_list)

    # --- Delete Flag Validation ---
    validate_delete_flags(delete_list)

    # --- Equal Length Validation ---
    validate_equal_lengths(
        FirstName=fname_list,
        LastName=lname_list,
        MiddleInitial=minit_list,
        Department=dept_input_list,
        Store=store_list,
        ThirdElement=thirdE_list,
        DeleteFlag=delete_list,
    )

    # --- Building output xlsx ---
    full_name_list = []
    for i in range(len(fname_list)):
        full_name_list.append(
            (fname_list[i] + " " + minit_list[i] + " " + lname_list[i])
        )

    outlist = [
        [
            "Delete?",
            "Item Name",
            "Department Code",
            "Sector #",
            "GL Account Code",
            "3rd Element - Category Code Code",
        ]
    ]

    for i in range(len(full_name_list)):
        for j in dictionary[dept_input_list[i]]:
            outlist.append(
                [
                    delete_list[i],
                    full_name_list[i],
                    dept_input_list[i],
                    store_list[i],
                    j,
                    thirdE_list[i],
                ]
            )

    df = pd.DataFrame(
        outlist,
        columns=[
            "DELETE",
            "NAME",
            "LEVEL_01_CODE",
            "LEVEL_02_CODE",
            "LEVEL_03_CODE",
            "LEVEL_04_CODE",
        ],
    )

    df.to_excel("output.xlsx", index=False, index_label=False, sheet_name="List")
