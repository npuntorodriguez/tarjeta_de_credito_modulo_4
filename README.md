Ejercicio individual
Objetivos

Practicar las convenciones para crear clases
Implementar argumentos por default
Practicar las estructuras de control
Crear y actualizar los atributos de una instancia a través de self
Probar las funcionalidades de desarrollo a través de la creación de instancias e invocación de métodos
De acuerdo a lo que vimos el capítulo anterior y conforme avanzamos en la aplicación, hemos notado que lo correcto sería asignar el saldo_pagar y el limite_credito a una tarjeta de crédito. Los usuarios pueden tener una (¡o muchas!) tarjetas de crédito y esas tarjetas son las que tienen el saldo y el límite. Eso entonces significa que tengamos que tener una clase dedicada a la TarjetaCredito. Como comentamos hace un momento, esta nueva clase no es independiente; ya que las tarjetas de crédito solo existen cuando los usuarios adquieren una.

Por lo pronto, en esta tarea pondremos en pausa la información del usuario. Ese será un desafío para el siguiente capítulo.

La clase TarjetaCredito debe tener un saldo_pagar. Cuando se crea una nueva instancia de TarjetaCredito se da el monto, de lo contrario el saldo_pagar se establece como $0. La tarjeta debe tener también un límite de crédito, que se va a proporcionar en la creación de la instancia. Por último, la tarjeta de crédito tendrá intereses, los cuales deben guardarse como decimales; por ejemplo: si tiene 2% de interés, se guardará 0.02. Esta información también debe enviarse al crear la instancia.

Nota: cuando utilizamos valores por default, el orden de los parámetros es de suma importancia.  

La clase debe incluir los siguientes métodos:

compra(self, monto): aumenta el saldo_pagar de acuerdo al monto recibido siempre y cuando la tarjeta de crédito no haya llegado a su límite crediticio. De lo contrario, que imprima: “Tarjeta Rechazada, has alcanzado tu límite de crédito”.
pago(self, monto): disminuye el saldo_pagar de la tarjeta.
mostrar_info_tarjeta(self): imprime en la consola el saldo a pagar de la tarjeta. Por ejemplo: “Saldo a Pagar: $100”
cobrar_interes(self): aumenta el saldo_pagar cobrando intereses. Es decir al saldo_pagar actual se le agregará el saldo_pagar * los intereses.

Crea la clase TarjetaCredito con los atributos de saldo_pagar, limite_credito, intereses
Crea el método compra para la clase TarjetaCredito
Crea el método pago para la clase TarjetaCredito
Crea el método mostrar_info_tarjeta para la clase TarjetaCredito
Crea el método cobrar_interes para la clase TarjetaCredito
Crea 3 tarjetas
Para la primera tarjeta, haz 2 compras y un pago. Luego cobra los intereses y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
Para la segunda tarjeta, haz 3 compras y 2 pagos. Luego cobra los intereses y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
Para la tercera tarjeta, haz 5 compras y excede su límite de crédito. Luego muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
BONUS: crea un método de clase para imprimir todas las instancias de la información de las tarjetas creadas. En el capítulo pasado te dimos algunas pistas de cómo realizarlo.