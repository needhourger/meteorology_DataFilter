#-*- coding:utf-8 -*-
import os
import json
import csv
import argparse
import logging
logging.basicConfig(format="%(asctime)s-[%(levelname)s]:%(message)s",level=logging.INFO)

BASE_PATH=os.path.split(os.path.abspath(__file__))[0]

def load_files():
    path=os.path.join(BASE_PATH,"data")
    logging.info("Scanning csv files in {}".format(path))
    for root,_,files in os.walk(path):
        for f in files:
            logging.info(f)
            yield os.path.join(root,f)

def get_city_pos(headers,cities):
    ret=[]
    for c in cities:
        try:
            index=headers.index(c)
            ret.append(index)
        except:
            # logging.warning("error city name {}".format(c))
            continue
    return set(ret)

def generate_date(files,cities,types,hours,f_out):
    logging.info("Generate data...")
    for f in files:
        logging.info("Handle {}".format(f))
        with open(f,"r",encoding="utf-8") as f:
            f_csv=csv.reader(f)
            headers=next(f_csv,None)
            # print(headers)
            pCitys=get_city_pos(headers,cities)
            # print(pCitys)
            for row in f_csv:
                # print(row)
                if len(row)>3 and int(row[1]) in hours and row[2] in types:
                    new_row=[row[0],row[1],row[2]]
                    for p in pCitys:
                        new_row.append(row[p])
                        f_out.writerow(new_row)

def init_output(cities):
    path=os.path.join(BASE_PATH+"/output/result.csv")
    headers=["date","hour","type"]
    headers.extend(cities)
    logging.info("Save to {}".format(path))
    f=open(path,"w+",encoding="utf-8",newline="")
    f_csv=csv.writer(f)
    f_csv.writerow(headers)
    return f_csv

def main():
    parser=argparse.ArgumentParser(description="Date Filter - 数据筛选器")
    parser.add_argument(
        "-c",
        "--city",
        dest="cities",
        type=str,
        nargs="*",
        default=("北京",),
        help="筛选城市，以空格分隔"
    )
    parser.add_argument(
        "-t",
        "--type",
        dest="types",
        type=str,
        nargs="*",
        default=("PM2.5",),
        help="筛选数据参数，以空格分隔"
    )
    parser.add_argument(
        "--hour",
        dest="hours",
        type=int,
        nargs="*",
        default=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23),
        help="筛选小时，以空格分隔，默认全天"
    )
    args=parser.parse_args()
    cities=args.cities
    types=args.types
    hours=args.hours
    print(cities)
    print(types)
    print(hours)
    input()

    files=load_files()
    f_csv=init_output(cities)
    generate_date(files,cities,types,hours,f_csv)
    

if __name__ == "__main__":
    main()