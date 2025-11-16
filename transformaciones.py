def crear_columna_ratio(df, num, den):
    df_ratio = df.copy()
    df_ratio[den] = df_ratio[den].replace(0, float("nan"))
    nueva_columna = f"{num}_sobre_{den}"
    df_ratio[nueva_columna] = df_ratio[num] / df_ratio[den]

    return df_ratio

def filtrar_por_rango(df, columna, minimo, maximo):
    df_filtrado = df.copy()
    df_filtrado = df_filtrado[
        (df_filtrado[columna] >= minimo) &
        (df_filtrado[columna] <= maximo)
    ]
    
    return df_filtrado
