def normalizar (df, columna):
    df_normalizado = df.copy()
    df_normalizado[columna] = (df_normalizado[columna] - df_normalizado[columna].mean()) / df_normalizado[columna].std()

    return df_normalizado

def estandardizar(df, columna):
    df_estand = df.copy()
    df_estand[columna] = (df_estand[columna] - df_estand[columna].min()) / (df_estand[columna].max() - df_estand[columna].min())

    return df_estand
    