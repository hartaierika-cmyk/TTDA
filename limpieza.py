def reemplazar(df, columna):

    df_rpmedia = df.copy()
    media = df_rpmedia[columna].mean()
    df_rpmedia[columna] = media
    
    return df_rpmedia