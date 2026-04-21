from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Buscar el campo Correo electrónico y rellenarlo
driver.find_element(By.ID, "email").send_keys("correo@gmail.com")

# Buscar el campo Contraseña y rellenarlo
driver.find_element(By.ID, "password").send_keys("contraseña")

# Buscar el botón Iniciar sesión y hacer clic en él
driver.find_element(By.XPATH, ".//*[@class='auth-form__button']").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# Buscar el pie de página
footer = driver.find_element(By.TAG_NAME, "footer")

# Desplazar el pie de página a la vista
driver.execute_script("arguments[0].scrollIntoView();", footer)

# Comprobar que el pie de página contiene el string 'Around'
assert "Around" in footer.text

driver.quit()
