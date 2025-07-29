class exclude_column_define:
    exclude_column_list = {
        "test_table": [
            "test_column_2",
            "test_column_4"
        ]
    }

def IsExcludedColumn(tableName:str, columnName:str) -> bool:
        if tableName in exclude_column_define.exclude_column_list:
            if columnName in exclude_column_define.exclude_column_list[tableName]:
                return True
            else:
                return False

