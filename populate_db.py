import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','diagnospymes.settings')
import django
django.setup()
from mm_evaluation.models import *

mps = [None for i in range(11)]
pcs = []

mps[1] = Macroprocess(name='Manejo del Almacén', number=1)

pcs.append(
    Process(macroprocess_id=mps[1],
    name='Distribución de espacios de almacenamiento',
    description='Hace referencia al control y vigilancia de los espacios que se utilizan dentro de la organización para el almacenamiento de materia prima, insumos y producto terminado.',
    guiding_question='¿Como es la gestión de los espacios que se utilizan para almacenar materia prima y producto terminado?',
    weight=0.25)
)

pcs.append(
    Process(macroprocess_id=mps[1],
    name='Transporte materia prima, insumos y producto',
    description='Se refiere a los elementos, guías y métodos utilizados para el traslado de una ubicación a otra de materias primas, insumos, producto en proceso y producto terminado',
    guiding_question='¿Cómo es el transporte de materia prima o producto terminado que será almacenado o que se va a retirar de almacenamiento?',
    weight=0.25)
)

pcs.append(
    Process(macroprocess_id=mps[1],
    name='Gestión de órdenes del almacén',
    description='Hace referencia al manejo que se les da a las órdenes de producción y por ende a las órdenes para realizar una extracción de materias primas e insumos del almacén de forma ordenada y que mejore el flujo de materiales por la empresa.',
    guiding_question='¿Como es la manera en la que se priorizan, ordenan y muestran las ordenes o solicitudes para retirar materia prima/producto de los lugares de almacenamiento?',
    weight=0.25)
)

pcs.append(
    Process(macroprocess_id=mps[1],
    name='Picking - Preparación de pedidos',
    description='Hace referencia al proceso de extraer de las posiciones de almacenamiento materiales o producto y que tan simple o complicado se hace ello.',
    guiding_question='¿Se utilizan estrategias para planear y/o realizar la extracción de materia prima o producto terminado de los lugares de almacenamiento?',
    weight=0.25)
)
mps[2] = Macroprocess(name='Manejo de Inventarios', number=2)

pcs.append(
    Process(macroprocess_id=mps[2],
    name='Control de niveles de inventarios',
    description='Hace referencia al proceso de revisión y comparación física de los niveles de inventario tanto de materia prima como de producto terminado en los lugares designados para almacenar',
    guiding_question='¿Cómo y con qué estrategias se revisa la cantidad de materia prima o producto terminado que la empresa tiene?',
    weight=0.2)
)

pcs.append(
    Process(macroprocess_id=mps[2],
    name='Orden y mantenimiento de inventarios',
    description='El proceso ha referencia a como los encargados de la empresa hacen mantenimiento y aseguran un orden lógico y adecuado a los inventarios para que sea fácil acceder a ellos y sea agradable a la vista al no haber desorden',
    guiding_question='¿Cómo se ordenan los inventarios de modo que sean de fácil acceso y ubicación tanto físicamente como en el sistema de manejo de inventarios que se tenga?',
    weight=0.2)
)

pcs.append(
    Process(macroprocess_id=mps[2],
    name='Sistematización de los inventarios',
    description='Se refiere al manejo de los inventarios desde la teoría y desde lo digital: el control de niveles, ubicaciones, calidad, proveedores, clientes y todo lo que se relacione con los inventarios, al ser esta información un reflejo fiel de lo físico.',
    guiding_question='¿Cómo y con que se maneja la información de los inventarios físicos de materia prima y/o producto terminado?',
    weight=0.2)
)

pcs.append(
    Process(macroprocess_id=mps[2],
    name='Reabastecimiento de inventarios',
    description='El proceso contrario al picking, hace referencia de cómo se cargan las posiciones de almacenamiento con materiales y productos. También se conoce como putaway o replenishment a la acción de almacenar inventarios. ',
    guiding_question='¿Cómo se hace ingresan los productos y la materia prima al inventario físico?',
    weight=0.2)
)

pcs.append(
    Process(macroprocess_id=mps[2],
    name='Control de calidad de los inventarios',
    description='El proceso que consiste en no solamente revisar los inventarios, sino asegurarse que se encuentren con la calidad esperada y que asegure su funcionalidad, que en el caso de productos o materiales perecederos todavía se encuentren hábiles para su aprovechamiento y uso.',
    guiding_question='¿Con que técnicas se realiza la revisión de la calidad de la materia prima y del producto que se encuentra en inventario?',
    weight=0.2)
)
mps[3] = Macroprocess(name='Abastecimiento', number=3)

pcs.append(
    Process(macroprocess_id=mps[3],
    name='Certificación a proveedores',
    description='Se refiere al proceso de asegurar que la empresa trabaje con proveedores de confianza y que cumplan con cierto nivel de exigencias a través de revisión de certificaciones o de que la propia empresa se encargue de certificar proveedores bajos unos estándares definidos internamente.',
    guiding_question='¿Cómo hace la empresa para certificar y asegurar la calidad de sus proveedores?',
    weight=0.165)
)

pcs.append(
    Process(macroprocess_id=mps[3],
    name='Evaluación de proveedores',
    description='El proceso de evaluar en tiempo, costo, calidad y demás factores el desempeño de los proveedores a la hora de trabajar y alinearse con la empresa.',
    guiding_question='¿Cómo y bajo qué criterios se califican y evalúan a los proveedores?',
    weight=0.165)
)

pcs.append(
    Process(macroprocess_id=mps[3],
    name='Comunicación con proveedores',
    description='Hace referencia al proceso de comunicación por cualquiera que sea el medio con los proveedores que asegure no existan mal entendidos y que finalmente el servicio prestado por ellos sea mejor.',
    guiding_question='¿Cómo y a través de que medios y con qué frecuencia se comunica con los proveedores?',
    weight=0.165)
)

pcs.append(
    Process(macroprocess_id=mps[3],
    name='Trabajo colaborativo con proveedores',
    description='Se refiere al proceso de compartir y tener cada vez más cerca a los proveedores de la compañía, generar la confianza para compartir datos e información que provoquen una mejora en los niveles de servicio. Abordar más de cerca los conceptos de cadena de suministro al interactuar constantemente para mejorar.',
    guiding_question='¿Como se llevan a cabo los proyectos o actividades conjuntas con los proveedores?',
    weight=0.165)
)

pcs.append(
    Process(macroprocess_id=mps[3],
    name='Sistema para la gestión de proveedores',
    description='El proceso que refiere al cómo la empresa registra toda la información referente a los proveedores, así como cotizaciones y demás que le permitan tomar decisiones y estar enterado sobre quiénes son sus proveedores. No necesariamente es un sistema digital.',
    guiding_question='¿Cómo se maneja la información de los diferentes proveedores?',
    weight=0.165)
)

pcs.append(
    Process(macroprocess_id=mps[3],
    name='Compras',
    description='Se refiere a todo el proceso que involucra la compra de materiales, servicios y demás, así como la negociación y las estrategias que utiliza la empresa para asegurar comprar cantidad y calidad en los momentos adecuados para evitar futuros desperdicios.',
    guiding_question='¿Cómo es el proceso de compra/adquisición de bienes y servicios?',
    weight=0.165)
)
mps[4] = Macroprocess(name='Distribución & Servicio al Cliente', number=4)

pcs.append(
    Process(macroprocess_id=mps[4],
    name='Servicio posventa',
    description='Hace referencia al proceso de mantener contacto con los clientes tiempo después de su adquisición, ya sea que existan canales para ello. El tiempo durante el cual se ofrece el servicio y en qué condiciones son elementos claves a considerar del proceso.',
    guiding_question='¿Se hace y como contacto con los clientes una vez adquieren los productos para asegurar el mejor servicio?',
    weight=0.2)
)

pcs.append(
    Process(macroprocess_id=mps[4],
    name='Rastreo de pedidos enviados',
    description='El proceso de tener vigilancia y control sobre los productos que salen de la empresa. Los productos saliente no solo se limitan a la distribución de pedidos, sino también a devoluciones y demás.',
    guiding_question='¿Se lleva y como una trazabilidad de todo producto propiedad de la empresa que se encuentra siendo transportada?',
    weight=0.2)
)

pcs.append(
    Process(macroprocess_id=mps[4],
    name='Garantía de la satisfacción cliente',
    description='Hace referencia a los esfuerzos ejecutados por la empresa para asegurar que el cliente reciba un producto con la calidad esperada.',
    guiding_question='¿Se ofrece y de que tipo garantías a los clientes ante producto con defectos o por no conformidad ante el mismo?',
    weight=0.2)
)

pcs.append(
    Process(macroprocess_id=mps[4],
    name='Distribución de pedidos',
    description='El proceso de entrega y distribución de los pedidos ya sea a través de una flota propia, tercerizada o mixta a los distintos clientes con los que cuente la organización.',
    guiding_question='¿Cómo se realizan las entregas de productos a los clientes?',
    weight=0.2)
)

pcs.append(
    Process(macroprocess_id=mps[4],
    name='Devoluciones de producto',
    description='Se refiere a la logística inversa, es decir la manera en la que la empresa recibe y procesa las devoluciones por calidad de su producto.',
    guiding_question='¿Cómo se manejan los pedidos que se devuelven por tema de calidad o de conformidad?',
    weight=0.2)
)
mps[5] = Macroprocess(name='Planeación Estratégica', number=5)

pcs.append(
    Process(macroprocess_id=mps[5],
    name='Planeación de demanda - Pronósticos',
    description='Hace referencia a las técnicas que utiliza la empresa para prever las ventas de acuerdo con datos históricos pasados, que ayuden a determinar comportamientos futuros.',
    guiding_question='¿Cómo se realizan los pronósticos de ventas?',
    weight=0.25)
)

pcs.append(
    Process(macroprocess_id=mps[5],
    name='Planeación oferta - Plan de producción',
    description='Se refiere al proceso de planear los recursos necesarios para ejecutar la producción a corto y mediano plazo de acuerdo con proyecciones realizadas. Involucra desde capacidad del personal, de la maquinaria, así como los costos asociados a ello.',
    guiding_question='¿Cómo se realizan los planes de producción de la empresa?',
    weight=0.25)
)

pcs.append(
    Process(macroprocess_id=mps[5],
    name='Estimaciones de crecimiento',
    description='Hace referencia a planear y establecer una meta del crecimiento de la empresa, plantear estrategias y actividades del día a día que apunten a esa meta. El crecimiento como el buscar más que el solo sostenimiento económico.',
    guiding_question='¿Cómo se planea el crecimiento económico y productivo de la empresa?',
    weight=0.25)
)

pcs.append(
    Process(macroprocess_id=mps[5],
    name='Planeación de expansión física',
    description='Se refiere a la gestión actual de la infraestructura física de la empresa y las proyecciones que tiene en cuanto a su potencial utilización en el futuro para generar utilidades. Hace referencia también a plantear la necesidad de capacidad adicional de acuerdo con crecimiento de demanda esperados.',
    guiding_question='¿Cómo se planea la expansión de los espacios físicos a futuro?',
    weight=0.25)
)
mps[6] = Macroprocess(name='Manejo del Recurso Humano', number=6)

pcs.append(
    Process(macroprocess_id=mps[6],
    name='Motivación y desempeño de empleados',
    description='Hace referencia al control sobre la motivación y el desempeño actual de los empleados en los lugares y puestos donde se encuentran trabajando ',
    guiding_question='¿Cómo se mide la motivación que tienen los diferentes empleados y colaboradores de la empresa?',
    weight=0.165)
)

pcs.append(
    Process(macroprocess_id=mps[6],
    name='Capacitaciones al personal',
    description='Se refiere al proceso de capacitar y mantener actualizados en conocimientos del área al personal para asegurar que la empresa sea competitiva desde su recurso humano.',
    guiding_question='¿Cómo y cada cuanto se realizan capacitaciones/talleres/cursos para mantener actualizados a los empleados?',
    weight=0.165)
)

pcs.append(
    Process(macroprocess_id=mps[6],
    name='Control niveles de estudio del personal',
    description='El proceso se refiere a la vigilancia que hace la empresa sobre las aptitudes y el nivel educativo con el que cuenta cada uno de los empleados para asignarle tareas correspondientes con sus verdaderas capacidades.',
    guiding_question='¿Cómo se controla que los empleados tengan el nivel educativo adecuado para el puesto que desempeñan?',
    weight=0.165)
)

pcs.append(
    Process(macroprocess_id=mps[6],
    name='Adecuación lugares de trabajo',
    description='El proceso de asegurar que los lugares de trabajo sean adecuados para las tareas que allí se realizan en temas de orden, limpieza, disponibilidad y ergonomía. ',
    guiding_question='¿Cómo se tienen organizados los diferentes puestos de trabajo de los empleados?',
    weight=0.165)
)
mps[7] = Macroprocess(name='Ventas', number=7)

pcs.append(
    Process(macroprocess_id=mps[7],
    name='Estrategias y nivel de venta',
    description='Hace referencia a todas las estrategias de mercadeo utilizadas para vender y su respectivo impacto generado en ventas reales.',
    guiding_question='¿Cómo y cuánto se vende respecto a lo que se esperaría vender?',
    weight=0.5)
)

pcs.append(
    Process(macroprocess_id=mps[7],
    name='Exportaciones',
    description='El proceso correspondiente a internacionalización y abarcar nuevos mercados con los productos ofrecidos, así como el proceso logístico que lleva a ello como los contactos, las investigaciones y el transporte.',
    guiding_question='¿Cómo se exporta?',
    weight=0.5)
)
mps[8] = Macroprocess(name='Producción', number=8)

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Balanceo de líneas de producción',
    description='Hace referencia al proceso de identificar cuellos de botella en el proceso productivo y su correcto balanceo de cargas para equilibrar el sistema.',
    guiding_question='¿Como se asignan las tareas operativas para que sean igualmente justas?',
    weight=0.125)
)

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Flexibilidad del proceso productivo',
    description='Se refiere a los esfuerzo realizados por la empresa para cumplir a nivel productivo de manera ágil con los cambios en las necesidades de los clientes y poder entregar a ellos lo que requieren.',
    guiding_question='¿Cómo se les facilita flexibilidad a los procesos, ante las necesidades del mercado?',
    weight=0.125)
)

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Control de la producción',
    description='Se refiere al nivel de control que tiene el encargado de la producción sobre ella, que le permite tomar decisiones clave como el tipo, cantidad, calidad, y demás parámetros de la producción de forma rápida y efectiva.',
    guiding_question='¿Cómo se controla la cantidad y el tipo de producto que se producen en determinados momentos?',
    weight=0.125)
)

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Comunicación de información',
    description='El proceso corresponde al manejo y transmisión de información a nivel de producción que permite a la empresa estar en la misma página sobre todo a nivel operativo con los niveles estratégico y táctico, evitando errores por desalineamiento.',
    guiding_question='¿Cómo se maneja y comunica la información de producción a todos los relacionados?',
    weight=0.125)
)

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Estandarización de procesos',
    description='Corresponde a los esfuerzo y estrategias utilizados por la empresa para facilitar y agilizar los procesos productivos al adicionalmente simplificar su oferta de producto.',
    guiding_question='¿Cómo se busca estandarizar/facilitar los procesos productivos?',
    weight=0.125)
)

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Costeo de producción',
    description='Se refiere al proceso de identificar los diferentes costos y gastos que involucra la transformación de materiales: mano de obra, compras e indirectos, y la gestión para disminuirlos sin afectar el producto.',
    guiding_question='¿Cómo se calculan los costos y gastos relativos al proceso productivo?',
    weight=0.125)
)

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Control de calidad producción',
    description='Hace referencia a las técnicas utilizadas por la empresa para asegurar la calidad del producto desde la misma producción y evitar que posibles errores que se generen se sigan generando y produciendo.',
    guiding_question='¿Con que técnicas se realiza la revisión de la calidad de los productos que se van produciendo o se produjeron?',
    weight=0.125)
)

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Reprocesamiento',
    description='El proceso hace referencia a todos los productos que por motivos de calidad no pudieron salir a la venta o que salieron y fueron retornados por los mismos temas de calidad, que se vuelven a procesar para que no se conviertan en desechos totalmente y poder generar algo de rentabilidad de ellos.',
    guiding_question='¿Cómo se manejan los productos defectuosos que deben ser reprocesados?',
    weight=0.125)
)
mps[9] = Macroprocess(name='Organizacional', number=9)

pcs.append(
    Process(macroprocess_id=mps[9],
    name='Colaboración interempresarial',
    description='Se refiere como la empresa se relaciona, trabaja, asocia y alinea con otras empresas que le permita utilizarlas como apalancamiento para la mejora de su competitividad. El apalancamiento para la competitividad se hace mutuamente.',
    guiding_question='¿Cómo es la colaboración y la ayuda con y por parte de otras empresas?',
    weight=0.142)
)

pcs.append(
    Process(macroprocess_id=mps[9],
    name='Financiación',
    description='El proceso hace referencia a la búsqueda de la empresa por financiar las ideas que se tengan en pro de la mejora empresarial, tanto con entidades públicas y privadas. Asimismo se refiere a todo el proceso de estudio que se requiere previo a solicitar una financiación.',
    guiding_question='¿Cómo busca la empresa financiar los proyectos y las ideas que tiene?',
    weight=0.142)
)

pcs.append(
    Process(macroprocess_id=mps[9],
    name='Apropiamiento tecnológico e Industria 4.0',
    description='Hace referencia a la apropiación y tendencia al uso e incorporación de infraestructura tecnológica y referente a la cuarta revolución industrial en los procesos productivos como una ventaja competitiva que ayude al marginamiento de la empresa.',
    guiding_question='¿Cómo es la gestión de la tecnología y la aproximación a industria 4.0 en la empresa?',
    weight=0.142)
)

pcs.append(
    Process(macroprocess_id=mps[9],
    name='Innovación',
    description='El proceso corresponde a todas las acciones novedosas y diferentes que nacen como ideas desde el personal de la empresa y que se terminan ejecutando para finalmente generar algún tipo de beneficio.',
    guiding_question='¿Cómo se gestionan las ideas innovadoras para la mejora de la empresa?',
    weight=0.142)
)

pcs.append(
    Process(macroprocess_id=mps[9],
    name='Distribución de tiempo',
    description='Hace referencia a la planeación del tiempo tanto de individuos como de colectivos para cumplir con las actividades diarias de la empresa.',
    guiding_question='¿Cómo se distribuye el tiempo para cumplir con las necesidades del día a día?',
    weight=0.142)
)

pcs.append(
    Process(macroprocess_id=mps[9],
    name='Cultura organizacional',
    description='Se refiere al proceso de idear estrategias que aseguren que el personal se apropie de la empresa para asegurar que cuiden y apoyen el crecimiento de la empresa, así como el mantener el recurso humano dentro de la misma.',
    guiding_question='¿Cómo es la cultura y el sentido de pertenencia de los empleados de la empresa?',
    weight=0.142)
)

pcs.append(
    Process(macroprocess_id=mps[9],
    name='I+D de productos y servicios nuevos',
    description='El proceso que corresponde con la investigación y generación de nuevas ideas de productos y servicios, así como su posterior desarrollo y lanzamiento, que aseguren a la empresa una diversificación del catálogo de productos y una permanencia en el mercado.',
    guiding_question='¿Cómo es el proceso de investigación y desarrollo de nuevos productos?',
    weight=0.142)
)
mps[10] = Macroprocess(name='Externas', number=10)

pcs.append(
    Process(macroprocess_id=mps[10],
    name='Respuesta a políticas gubernamentales',
    description='El proceso se refiere a como la empresa anticipa y se prepara para responder a políticas establecidas por los gobiernos locales. Adicionalmente los planes de respaldo con los que cuenta a situaciones que puedan ser extremas y que pongan a prueba la resiliencia empresarial.',
    guiding_question='¿Cuál es la reacción de la empresa ante políticas de gobierno que la afectan?',
    weight=0.33)
)

pcs.append(
    Process(macroprocess_id=mps[10],
    name='Estabilidad económica de la empresa',
    description='Se refiere al proceso de asegurar que a pesar de las inestabilidades geopolíticas y económicas de los gobiernos locales, la empresa cuente con la solidez para sobrevivir y salir delante a pesar de ello. Igualmente corresponde a la búsqueda de independencia empresarial y económica.',
    guiding_question='¿Cuál es el nivel de estabilidad e independencia económica que tiene la empresa?',
    weight=0.33)
)

pcs.append(
    Process(macroprocess_id=mps[10],
    name='Participación en iniciativas públicas',
    description='El proceso que corresponde con la participación en iniciativas y programas públicos que se desarrollan localmente para apoyar a la micro y pequeña empresa en su desarrollo. Corresponde también a la financiación, la excepción de impuestos o cualquier otra ayuda adicional dada por el gobierno para aportar al crecimiento de las pequeñas empresas en el país.',
    guiding_question='¿Cuál es el nivel de participación de la empresa en iniciativas y programas públicos para la mejora de la competitividad de empresas?',
    weight=0.33)
)


for mp in mps[1:]:
    mp.save()

for p in pcs[1:]:
    p.save()