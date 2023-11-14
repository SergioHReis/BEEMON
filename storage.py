from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
import json

Base = declarative_base()

class Quote(Base):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    author = Column(String)
    tags = Column(String)

def save_to_database(data):
    engine = create_engine('sqlite:///quotes.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        for item in data:
            quote = Quote(text=item['text'], author=item['author'], tags=', '.join(item['tags']))
            session.add(quote)
        session.commit()

def create_dataframe(data):
    df = pd.DataFrame(data)
    df.to_csv('quotes_dataframe.csv', index=False)
    print(df)

def save_to_json(data):
    with open('quotes_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
