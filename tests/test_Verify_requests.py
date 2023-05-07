    # Verificar que la función devuelva el resultado correcto para cada URL bloqueada 
    for url in urls_bloqueadas: 
        self.assertEqual(block_url(url), "No se puede acceder a esta página.") 
        
def test_keyword_matching(self): 
    # Crear una lista de palabras clave para probar el código 
    palabras_clave = ["password", "credit card"] 
    
    # Verificar que la función devuelva el resultado correcto para cada palabra clave  
    for palabra in palabras_clave: 
        contenido = f"El contenido contiene la palabra {palabra}" 
        self.assertEqual(check_keywords(palabra, contenido), f"La palabra clave '{palabra}' está en el contenido. Acceso denegado.")
