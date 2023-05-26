import json
import pandas as pd


def db_statistics(path_to_json: str) -> dict[str, int]:
    db_2_queries_num = {}
    with open(path_to_json) as train_file:
        train_data = json.load(train_file)
        for cur_item in train_data:
            db_id = cur_item["db_id"]
            db_2_queries_num[db_id] = db_2_queries_num.get(db_id, 0) + 1

    return db_2_queries_num


def create_csv_dataset(path_to_json: str, path_to_csv: str) -> None:
    data4csv = []
    with open(path_to_json) as train_file:
        train_data = json.load(train_file)
        for cur_item in train_data:
            db_id = cur_item["db_id"]
            question = cur_item["question"]
            sql = cur_item["SQL"]
            data4csv.append([question, sql])

    df = pd.DataFrame(data4csv, columns=["question", "sql"])
    df.to_csv(path_to_csv, sep=',', index=False)


stats = db_statistics(path_to_json="datasets/BIRD/train/train.json")
print(stats)
print(len(stats))
create_csv_dataset(path_to_json="datasets/BIRD/train/train.json",
                   path_to_csv="datasets/BIRD/train/train_initial.csv")

print("OK")
