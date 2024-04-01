import pandas as pd
import pathlib


def read_file(filename: str) -> pd.DataFrame:

    file_extension = pathlib.Path(filename).suffix

    if file_extension != ".csv":
        raise Exception("Not CSV file!")

    return pd.read_csv(
        filepath_or_buffer=f'csv_files/{filename}',
        encoding='latin-1',
    )


df = read_file("version_test.csv")

# Убираем Nan
df.dropna(inplace=True)

df_columns = df.columns

unnamed_col_name = df_columns[0]
sqrt_col_name = df.columns[-1]
values_col_name = df.columns[-2]

# Удаляем лишний столбец
df.drop([unnamed_col_name], axis=1, inplace=True)

# Переименование столбцов
df.rename(
    columns={sqrt_col_name: "Корень", values_col_name: "values"},
    inplace=True
)

# Привести столбцы к нужным типам данных
df["Корень"] = df["Корень"].str.replace(',', '.').astype(float)

# Группировка
result = df.groupby(df.columns).sum()

df_2 = pd.DataFrame({"x1": ["x1 1"], "new_columns": "ok"})

# Merge
merged_df = pd.merge(df, df_2, on="x1")

print(merged_df)
