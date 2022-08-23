from lexer import lexer
from tokens import token

if __name__ == '__main__':
    input = """
            instance DIA_ONAR_PERM(C_INFO)
            {
                npc = bau_900_onar;
                nr = 1;
                permanent = TRUE;
                description = "Czy na farmie wszystko w porządku?";
            };
        
            func void dia_onar_perm_info()
            {
                if(other.guild == GIL_NONE)
                {
                    AI_Output(self,other,"DIA_Onar_PERM_14_01");	//A co cię to obchodzi, przecież tutaj nie pracujesz.
                };
            }
            """

    l = lexer.Lexer(input)
    tok = l.next_token()

    while tok and tok.type != token.EOF:
        print("{} {}".format(tok.type, tok.literal))
        tok = l.next_token()
