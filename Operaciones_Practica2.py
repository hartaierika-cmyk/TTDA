def elimina_decimales(df, col):
    df[col + "_sin_decimales"] = df[col].astype(int)
    return df

def caluclaRatio(df, col1, col2):
    ratio = df[col1] / df[col2]
    if (ratio > 1).any():
        raise Exception("Algún valor del ratio es mayor que 1.")
    return ratio