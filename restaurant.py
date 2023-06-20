import funciones_restaurant as fn

#funciones: validaciones si o si!
#funciones: DESARROLLO OPCIONES!

while True:
    fn.mostrar_menu()
    opcion=fn.validar_opcion()
    if opcion==1:
        fn.ver_restaurant()
    elif opcion==2:
        fn.reserva()
    elif opcion==3:
        pass
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        break