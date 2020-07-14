# safe_passw
Este script python, gera senhas aleatórias e seguras //  This python script generates random and secure passwords

Safe Passw

Este script tem como funcionalidade principal a
geração de senhas seguras e completamente aleatórias
e distintas umas das outras.

Ele gera 3 caractéres aleatórios para cada 1 caractér 
digitado, dentre os valores que serão randomizados existem
símbolos, números e letras.

As senha se iniciam sempre com o termo "init", ou seja, 
uma senha mediana com 9 caractéres, vai ter um tamanho
final de 31 caractéres.

Exemplo:
            senha original: python123
            senha segura:   initc7&*#%3jdd?/i0lo0>ahl/4r>oy

                    
                    -----||-----


Para aqueles com interesse em alterações no código-fonte:

A string "aleatory_chars", contém os valores que serão 
randomizados.

Já na 7ª linha, o laço for utilizado randomiza os 3 digitos
para cada caracter inicial, utilizando a função "choice" do
módulo random.


---------------------------------------------------------------------------------------------------------
=========================================================================================================
---------------------------------------------------------------------------------------------------------


Safe Passw

This script has as main functionality the
generation of secure and completely random passwords
and distinct from each other.

It generates 3 random characters for each 1 character
typed, among the values ​​that will be randomized there are
symbols, numbers and letters.

Passwords always start with the term "init", that is,
an average password with 9 characters, it will have a length
end of 31 characters.

Example:
            original password: python123
            secure password: initc7&*#%3jdd?/i0lo0>ahl/4r>oy

                    
                    ----- || -----


For those interested in changes to the source code:

The string "random_chars", contains the values ​​that will be
randomized.

In the 7th line, the loop is used to randomize the 3 digits
for each initial character, using the "choice" function of the
random module.
