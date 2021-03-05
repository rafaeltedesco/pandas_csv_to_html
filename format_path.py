import pandas as pd
import os

def _format_path(path):
    return '\\'.join(path.replace('\\', ' ').split())

def pandarize(path, filename):
    """
        filename: str (.csv)
    """
    path = _format_path(path)
    return pd.read_csv(os.path.join(path,filename))


def format_date_time(df, column):
     return pd.to_datetime(df[column].str.upper(), format='%Y-%m-%d %I:%M %p')

def order_date_time(df, column):
    return df.sort_values(by=column, ascending=True)


def filter_by_columns(df, *columns):
    """
        df: pandas DataFrame
        columns: str args separeted by comma
        e.g 'price', 'address'

    """
    new_df = pd.DataFrame()

    for column in columns:
        new_df[column] = df[column]

    return new_df                                            

def generate_html(df, filename='students_ordered.html'):
    df.to_html(filename)

def get_format_df(path=r'C:\Users\Rafael\Downloads', filename='events-export.csv'):
    date_column = 'Start Date & Time'
    df = pandarize(path, filename)
    date_df = format_date_time(df, date_column)
    new_df = df.iloc[:,:]
    new_df[date_column] = date_df
    ordered_df = order_date_time(new_df, date_column)
    filtered_df = filter_by_columns(ordered_df, 'Invitee Name', 'Start Date & Time')
    generate_html(filtered_df)
    print('HTML file created with success')
    return filtered_df
    
df = get_format_df()
