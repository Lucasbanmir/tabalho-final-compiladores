# Generated from C:/Users/lucas/Documents/trabalho final compiladores\trabalhoFinal_lucas.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from gen.trabalhoFinal_lucasParser import trabalhoFinal_lucasParser
else:
    from gen.trabalhoFinal_lucasParser import trabalhoFinal_lucasParser
from jasmin import Jasmin, Id
from Erros import ErroTipoIncompativelDecl, ErroTipoInesperado, ErroTipoNaoInformado, ErroBreak, ErroDeclaracaoJaFeita, \
    ErroVariavelNaoDeclarada, ErroTipoExpressao, ErroTipoExpressaoDiferenteDeIncremento, ErroRetorno, \
    ErroDuplaExpressao, ErroArgumentoEsperado, ErroDeclaracaoDepoisDoBloco

# This class defines a complete listener for a parse tree produced by trabalhoFinal_lucasParser.
class trabalhoFinal_lucasListener(ParseTreeListener):

    # tabela de simbolos // refatorar: usar só uma, se nao da problema no gerador
    tabelaDeSimbolos = {}
    tabelaDeSimbolos_copy = {}

    # bloco de pilha
    blocoDePilha = []

    # argumentos de funcoes
    argumentoDeFuncoes = {}

    # bloco de funcoes com retorno tipado
    blocoRetorno = []

    # controla escopo da execucao: true para escopo local e false para escopo global
    controle_escopo = False
    # controla o endereço de instancia de nova variavel
    controle_endereco_novo = 0

    # flag para controlar se entrou em um calculo de expressao e impedir que jasmin duplique escrita no .j
    controleCalculoExpr = False

    def __init__(self, filename):
        self.jasmin = Jasmin(filename, self.tabelaDeSimbolos)
        self.label_id = 0

    # Enter a parse tree produced by trabalhoFinal_lucasParser#prog.
    def enterProg(self, ctx:trabalhoFinal_lucasParser.ProgContext):
        print("Iniciando análise semântica")
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#prog.
    def exitProg(self, ctx:trabalhoFinal_lucasParser.ProgContext):
        print("Finalizando análise semântica")
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#decVar.
    def enterDecVar(self, ctx:trabalhoFinal_lucasParser.DecVarContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#decVar.
    def exitDecVar(self, ctx:trabalhoFinal_lucasParser.DecVarContext):
        for token in ctx.listaIds().ID():
            if ctx.tipo().getText() == '<missing <INVALID>>':
                raise ErroTipoNaoInformado(ctx.start.line, token.getText())

            # se variavel existe e esta no escopo local, da erro
            if token.getText() in self.tabelaDeSimbolos and self.tabelaDeSimbolos[token.getText()].scope == self.controle_escopo:
                raise ErroDeclaracaoJaFeita(ctx.start.line, token.getText())

            # se a variavel ja estiver em escopo global, guarda ela para recuperar na saida da funcao de escopo local
            if token.getText() in self.tabelaDeSimbolos and self.tabelaDeSimbolos[token.getText()].scope == False:
                self.tabelaDeSimbolos_copy[token.getText()] = self.tabelaDeSimbolos[token.getText()]

            self.tabelaDeSimbolos[token.getText()] = Id(type=ctx.tipo().getText(), scope=self.controle_escopo, address=self.controle_endereco_novo)
            self.controle_endereco_novo += 1 # atualiza o proximo endereco disponivel
            self.jasmin.create(token.getText(), ctx.tipo().getText(), self.controle_escopo, False, 0)
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#decConst.
    def enterDecConst(self, ctx:trabalhoFinal_lucasParser.DecConstContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#decConst.
    def exitDecConst(self, ctx:trabalhoFinal_lucasParser.DecConstContext):
        for atrib in ctx.listaAtrib().atrib():
            id_token = atrib.ID()
            if ctx.tipo().getText() == '<missing <INVALID>>':
                raise ErroTipoNaoInformado(ctx.start.line, id_token.getText())

            # se variavel existe e esta no escopo local, da erro
            if id_token.getText() in self.tabelaDeSimbolos and self.tabelaDeSimbolos[id_token.getText()].scope == self.controle_escopo:
                raise ErroDeclaracaoJaFeita(ctx.start.line, id_token.getText())

            if id_token.getText() in self.tabelaDeSimbolos and self.tabelaDeSimbolos[id_token.getText()].scope == False:
                self.tabelaDeSimbolos_copy[id_token.getText()] = self.tabelaDeSimbolos[id_token.getText()]

            self.tabelaDeSimbolos[id_token.getText()] = Id(type=ctx.tipo().getText(), scope=self.controle_escopo,
                                                        address=self.controle_endereco_novo)
            self.controle_endereco_novo += 1  # atualiza o proximo endereco disponivel
            self.jasmin.create(id_token.getText(), ctx.tipo().getText(), self.controle_escopo, True, atrib.dado().getText())

            # verificar se o tipo atribuido da constante condiz com o valor inserido
            if ctx.tipo().getText() == 'int' and not atrib.dado().INT():
                raise ErroTipoIncompativelDecl(ctx.start.line, ctx.tipo().getText())
            elif ctx.tipo().getText() == 'real' and not atrib.dado().REAL():
                raise ErroTipoIncompativelDecl(ctx.start.line, ctx.tipo().getText())
            elif ctx.tipo().getText() == 'bool' and not atrib.dado().BOOL():
                raise ErroTipoIncompativelDecl(ctx.start.line, ctx.tipo().getText())
            elif ctx.tipo().getText() == 'String' and not atrib.dado().STRING():
                raise ErroTipoIncompativelDecl(ctx.start.line, ctx.tipo().getText())
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#tipo.
    def enterTipo(self, ctx:trabalhoFinal_lucasParser.TipoContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#tipo.
    def exitTipo(self, ctx:trabalhoFinal_lucasParser.TipoContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#listaIds.
    def enterListaIds(self, ctx:trabalhoFinal_lucasParser.ListaIdsContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#listaIds.
    def exitListaIds(self, ctx:trabalhoFinal_lucasParser.ListaIdsContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#listaAtrib.
    def enterListaAtrib(self, ctx:trabalhoFinal_lucasParser.ListaAtribContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#listaAtrib.
    def exitListaAtrib(self, ctx:trabalhoFinal_lucasParser.ListaAtribContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#atrib.
    def enterAtrib(self, ctx:trabalhoFinal_lucasParser.AtribContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#atrib.
    def exitAtrib(self, ctx:trabalhoFinal_lucasParser.AtribContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#funcBloco.
    def enterFuncBloco(self, ctx:trabalhoFinal_lucasParser.FuncBlocoContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#funcBloco.
    def exitFuncBloco(self, ctx:trabalhoFinal_lucasParser.FuncBlocoContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#decFuncao.
    def enterDecFuncao(self, ctx:trabalhoFinal_lucasParser.DecFuncaoContext):
        self.controle_escopo = True
        self.blocoDePilha.append('function')
        functionId = ctx.ID(0).getText()

        # se a funcao tem retorno de tipo entao deve verificar se tem funcao de retorno no bloco
        if len(ctx.ID()) <= len(ctx.tipo()):
            functionType = ctx.tipo(0).getText()
        else:
            functionType = None

        if functionId in self.tabelaDeSimbolos:
            raise ErroDeclaracaoJaFeita(ctx.start.line, functionId)

        self.tabelaDeSimbolos[functionId] = Id(type=functionType, scope=False, address=self.controle_endereco_novo)

        self.controle_endereco_novo += 1

        # verificando parametros da funcao
        args = []
        argsNames = []
        # se a funcao tem retorno de tipo entao deve verificar se tem funcao de retorno no bloco
        if len(ctx.ID()) <= len(ctx.tipo()):
            lista = list(zip(ctx.ID()[1:], ctx.tipo()[1:]))
        else:
            lista = list(zip(ctx.ID()[1:], ctx.tipo()[0:]))

        for id, Tipo in lista:
            # se variavel existe e esta no escopo local, da erro
            if id in self.tabelaDeSimbolos and self.tabelaDeSimbolos[id].scope == self.controle_escopo:
                raise ErroDeclaracaoJaFeita(ctx.start.line, id.getText())

            # se a variavel ja estiver em escopo global, guarda ela para recuperar na saida da funcao de escopo local
            if id.getText() in self.tabelaDeSimbolos and self.tabelaDeSimbolos[id.getText()].scope == False:
                self.tabelaDeSimbolos_copy[id.getText()] = self.tabelaDeSimbolos[id.getText()]

            self.tabelaDeSimbolos[id.getText()] = Id(type=Tipo.getText(), scope=self.controle_escopo,
                                                     address=self.controle_endereco_novo)
            self.controle_endereco_novo += 1
            args.append(Tipo.getText())
            argsNames.append(id.getText())

        self.argumentoDeFuncoes[functionId] = args
        self.jasmin.criaFuncao(functionId, argsNames)

        # se a funcao tem retorno de tipo entao deve verificar se tem funcao de retorno no bloco
        if len(ctx.ID()) <= len(ctx.tipo()):
            self.blocoRetorno.append(functionType)
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#decFuncao.
    def exitDecFuncao(self, ctx:trabalhoFinal_lucasParser.DecFuncaoContext):
        if len(self.blocoRetorno) > 0:
            self.blocoRetorno.pop()

        if len(self.blocoRetorno) > 0:
            raise ErroRetorno(ctx.start.line)

        self.jasmin.fechaFuncao()

        self.blocoDePilha.pop()

        for item in list(self.tabelaDeSimbolos):
            if self.tabelaDeSimbolos[item].scope:
                del self.tabelaDeSimbolos[item]

        for item in self.tabelaDeSimbolos_copy:
            self.tabelaDeSimbolos[item] = self.tabelaDeSimbolos_copy[item]

        # teste
        for item in self.tabelaDeSimbolos:
            print(item, ' => ', self.tabelaDeSimbolos[item].scope)
        print('----------')

        self.controle_escopo = False
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#main.
    def enterMain(self, ctx:trabalhoFinal_lucasParser.MainContext):
        self.jasmin.criaMain()
        self.controle_escopo = True
        self.blocoDePilha.append('function')
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#main.
    def exitMain(self, ctx:trabalhoFinal_lucasParser.MainContext):
        self.jasmin.fechaMain()
        self.blocoDePilha.pop()
        self.controle_escopo = False
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#comandos.
    def enterComandos(self, ctx:trabalhoFinal_lucasParser.ComandosContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#comandos.
    def exitComandos(self, ctx:trabalhoFinal_lucasParser.ComandosContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#comandosLoop.
    def enterComandosLoop(self, ctx:trabalhoFinal_lucasParser.ComandosLoopContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#comandosLoop.
    def exitComandosLoop(self, ctx:trabalhoFinal_lucasParser.ComandosLoopContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#break.
    def enterBreak(self, ctx:trabalhoFinal_lucasParser.BreakContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#break.
    def exitBreak(self, ctx:trabalhoFinal_lucasParser.BreakContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#decPrint.
    def enterDecPrint(self, ctx:trabalhoFinal_lucasParser.DecPrintContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#decPrint.
    def exitDecPrint(self, ctx:trabalhoFinal_lucasParser.DecPrintContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#decInput.
    def enterDecInput(self, ctx:trabalhoFinal_lucasParser.DecInputContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#decInput.
    def exitDecInput(self, ctx:trabalhoFinal_lucasParser.DecInputContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#for.
    def enterFor(self, ctx:trabalhoFinal_lucasParser.ForContext):
        # verificando primeiro parametro do for
        ctxId = ctx.ID().getText()
        # se variavel ja foi declarada, da erro
        if ctxId not in self.tabelaDeSimbolos:
            raise ErroVariavelNaoDeclarada(ctx.start.line, ctxId)
        # se declaracao nao for do tipo int, da erro
        if self.controle_escopo:
            if self.tabelaDeSimbolos[ctxId].type != 'int':
                raise ErroTipoInesperado(ctx.start.line, 'int', self.tabelaDeSimbolos[ctxId].type)


        # verifica se ID declarado é igual aos ids do incremento
        if ctxId != ctx.atribuicao().ID().getText():
            raise ErroTipoExpressaoDiferenteDeIncremento(ctx.start.line)


        print('break'';' in ctx.comandosLoop().__dict__)
        if ctx.ID() == None:
            ctxInt = ctx.INT()
            # print(ctxInt, self.tabelaDeSimbolos)
            self.jasmin.iniciaFor_com_valor(ctxInt, ctxId, 'break'';' in ctx.comandosLoop().__dict__, self.controle_escopo)
        else:
            ctxInt = self.tabelaDeSimbolos[ctx.ID().getText()].address
            # print(ctxInt, self.tabelaDeSimbolos)
            self.jasmin.iniciaFor(ctxInt, ctxId, 'break' in ctx.comandosLoop().__dict__, self.controle_escopo)

        ctx.stack_idx = len(self.blocoDePilha)

        # empilha flag loop para saber se entrou no loop
        self.blocoDePilha.append('loop')
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#for.
    def exitFor(self, ctx:trabalhoFinal_lucasParser.ForContext):
        # desempilha flag loop para saber se saiu do loop
        self.blocoDePilha.pop()

        ctxId = ctx.ID().getText()

        # print(ctxId)
        # print(ctx.expressao().val)
        # print(ctx.expressao().inh)
        # print(ctx.stack_idx)
        # print(ctx.incremento().op.text, ctx.incremento().INT())
        # print(ctx.funcao_break() == None)

        # ctxInt = self.tabelaDeSimbolos[ctx.ID(1).getText()].address
        # print(ctxInt, self.tabelaDeSimbolos)
        self.jasmin.exit_for(ctxId, ctx.expr().val, ctx.atribuicao().op.text, ctx.incremento().INT(), self.controle_escopo)
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#while.
    def enterWhile(self, ctx:trabalhoFinal_lucasParser.WhileContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#while.
    def exitWhile(self, ctx:trabalhoFinal_lucasParser.WhileContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#return.
    def enterReturn(self, ctx:trabalhoFinal_lucasParser.ReturnContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#return.
    def exitReturn(self, ctx:trabalhoFinal_lucasParser.ReturnContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#decAtrib.
    def enterDecAtrib(self, ctx:trabalhoFinal_lucasParser.DecAtribContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#decAtrib.
    def exitDecAtrib(self, ctx:trabalhoFinal_lucasParser.DecAtribContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#callFunc.
    def enterCallFunc(self, ctx:trabalhoFinal_lucasParser.CallFuncContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#callFunc.
    def exitCallFunc(self, ctx:trabalhoFinal_lucasParser.CallFuncContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#orOp.
    def enterOrOp(self, ctx:trabalhoFinal_lucasParser.OrOpContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#orOp.
    def exitOrOp(self, ctx:trabalhoFinal_lucasParser.OrOpContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#passTermo.
    def enterPassTermo(self, ctx:trabalhoFinal_lucasParser.PassTermoContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#passTermo.
    def exitPassTermo(self, ctx:trabalhoFinal_lucasParser.PassTermoContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#andOp.
    def enterAndOp(self, ctx:trabalhoFinal_lucasParser.AndOpContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#andOp.
    def exitAndOp(self, ctx:trabalhoFinal_lucasParser.AndOpContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#passTermo2.
    def enterPassTermo2(self, ctx:trabalhoFinal_lucasParser.PassTermo2Context):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#passTermo2.
    def exitPassTermo2(self, ctx:trabalhoFinal_lucasParser.PassTermo2Context):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#passTermo3.
    def enterPassTermo3(self, ctx:trabalhoFinal_lucasParser.PassTermo3Context):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#passTermo3.
    def exitPassTermo3(self, ctx:trabalhoFinal_lucasParser.PassTermo3Context):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#compOp.
    def enterCompOp(self, ctx:trabalhoFinal_lucasParser.CompOpContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#compOp.
    def exitCompOp(self, ctx:trabalhoFinal_lucasParser.CompOpContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#equalOp.
    def enterEqualOp(self, ctx:trabalhoFinal_lucasParser.EqualOpContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#equalOp.
    def exitEqualOp(self, ctx:trabalhoFinal_lucasParser.EqualOpContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#passTermo4.
    def enterPassTermo4(self, ctx:trabalhoFinal_lucasParser.PassTermo4Context):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#passTermo4.
    def exitPassTermo4(self, ctx:trabalhoFinal_lucasParser.PassTermo4Context):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#addMinusOp.
    def enterAddMinusOp(self, ctx:trabalhoFinal_lucasParser.AddMinusOpContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#addMinusOp.
    def exitAddMinusOp(self, ctx:trabalhoFinal_lucasParser.AddMinusOpContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#passTermo5.
    def enterPassTermo5(self, ctx:trabalhoFinal_lucasParser.PassTermo5Context):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#passTermo5.
    def exitPassTermo5(self, ctx:trabalhoFinal_lucasParser.PassTermo5Context):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#multiDivOp.
    def enterMultiDivOp(self, ctx:trabalhoFinal_lucasParser.MultiDivOpContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#multiDivOp.
    def exitMultiDivOp(self, ctx:trabalhoFinal_lucasParser.MultiDivOpContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#passTermo6.
    def enterPassTermo6(self, ctx:trabalhoFinal_lucasParser.PassTermo6Context):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#passTermo6.
    def exitPassTermo6(self, ctx:trabalhoFinal_lucasParser.PassTermo6Context):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#minusUniOp.
    def enterMinusUniOp(self, ctx:trabalhoFinal_lucasParser.MinusUniOpContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#minusUniOp.
    def exitMinusUniOp(self, ctx:trabalhoFinal_lucasParser.MinusUniOpContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#passTermo7.
    def enterPassTermo7(self, ctx:trabalhoFinal_lucasParser.PassTermo7Context):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#passTermo7.
    def exitPassTermo7(self, ctx:trabalhoFinal_lucasParser.PassTermo7Context):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#notOp.
    def enterNotOp(self, ctx:trabalhoFinal_lucasParser.NotOpContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#notOp.
    def exitNotOp(self, ctx:trabalhoFinal_lucasParser.NotOpContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#passFator.
    def enterPassFator(self, ctx:trabalhoFinal_lucasParser.PassFatorContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#passFator.
    def exitPassFator(self, ctx:trabalhoFinal_lucasParser.PassFatorContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#parenExprFat.
    def enterParenExprFat(self, ctx:trabalhoFinal_lucasParser.ParenExprFatContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#parenExprFat.
    def exitParenExprFat(self, ctx:trabalhoFinal_lucasParser.ParenExprFatContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#idFat.
    def enterIdFat(self, ctx:trabalhoFinal_lucasParser.IdFatContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#idFat.
    def exitIdFat(self, ctx:trabalhoFinal_lucasParser.IdFatContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#dadoFat.
    def enterDadoFat(self, ctx:trabalhoFinal_lucasParser.DadoFatContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#dadoFat.
    def exitDadoFat(self, ctx:trabalhoFinal_lucasParser.DadoFatContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#callFuncaoFat.
    def enterCallFuncaoFat(self, ctx:trabalhoFinal_lucasParser.CallFuncaoFatContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#callFuncaoFat.
    def exitCallFuncaoFat(self, ctx:trabalhoFinal_lucasParser.CallFuncaoFatContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#intDado.
    def enterIntDado(self, ctx:trabalhoFinal_lucasParser.IntDadoContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#intDado.
    def exitIntDado(self, ctx:trabalhoFinal_lucasParser.IntDadoContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#realDado.
    def enterRealDado(self, ctx:trabalhoFinal_lucasParser.RealDadoContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#realDado.
    def exitRealDado(self, ctx:trabalhoFinal_lucasParser.RealDadoContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#stringDado.
    def enterStringDado(self, ctx:trabalhoFinal_lucasParser.StringDadoContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#stringDado.
    def exitStringDado(self, ctx:trabalhoFinal_lucasParser.StringDadoContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#boolDado.
    def enterBoolDado(self, ctx:trabalhoFinal_lucasParser.BoolDadoContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#boolDado.
    def exitBoolDado(self, ctx:trabalhoFinal_lucasParser.BoolDadoContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#not.
    def enterNot(self, ctx:trabalhoFinal_lucasParser.NotContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#not.
    def exitNot(self, ctx:trabalhoFinal_lucasParser.NotContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#minusUni.
    def enterMinusUni(self, ctx:trabalhoFinal_lucasParser.MinusUniContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#minusUni.
    def exitMinusUni(self, ctx:trabalhoFinal_lucasParser.MinusUniContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#multiDiv.
    def enterMultiDiv(self, ctx:trabalhoFinal_lucasParser.MultiDivContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#multiDiv.
    def exitMultiDiv(self, ctx:trabalhoFinal_lucasParser.MultiDivContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#addMinus.
    def enterAddMinus(self, ctx:trabalhoFinal_lucasParser.AddMinusContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#addMinus.
    def exitAddMinus(self, ctx:trabalhoFinal_lucasParser.AddMinusContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#equal.
    def enterEqual(self, ctx:trabalhoFinal_lucasParser.EqualContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#equal.
    def exitEqual(self, ctx:trabalhoFinal_lucasParser.EqualContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#comp.
    def enterComp(self, ctx:trabalhoFinal_lucasParser.CompContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#comp.
    def exitComp(self, ctx:trabalhoFinal_lucasParser.CompContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#and.
    def enterAnd(self, ctx:trabalhoFinal_lucasParser.AndContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#and.
    def exitAnd(self, ctx:trabalhoFinal_lucasParser.AndContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#or.
    def enterOr(self, ctx:trabalhoFinal_lucasParser.OrContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#or.
    def exitOr(self, ctx:trabalhoFinal_lucasParser.OrContext):
        pass



del trabalhoFinal_lucasParser