from antlr4 import *
from gen.trabalhoFinal_lucasLexer import trabalhoFinal_lucasLexer
from gen.trabalhoFinal_lucasParser import trabalhoFinal_lucasParser
from gen.trabalhoFinal_lucasListener import trabalhoFinal_lucasListener
from Erros import *

from Erros import *

# This class defines a complete listener for a parse tree produced by trabalhoFinal_lucasParser.
class trabalhoFinal_lucasListener(ParseTreeListener):

    def __init__(self):
        self.symbolTable = {}  # tabela de símbolos global
        self.symbolTableLocal = {}  # tabela de símbolos local
        self.inFunction = False  # indica se estamos dentro de uma função
        self.currentFunctionType = None

    # Enter a parse tree produced by trabalhoFinal_lucasParser#prog.
    def enterProg(self, ctx:trabalhoFinal_lucasParser.ProgContext):
        print("Iniciando compilação")
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#prog.
    def exitProg(self, ctx:trabalhoFinal_lucasParser.ProgContext):
        print("Compilado com sucesso!")

        print("\nTabela de símbolos")
        print(self.symbolTable)
        print(self.symbolTableLocal)
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#decVar.
    def enterDecVar(self, ctx:trabalhoFinal_lucasParser.DecVarContext):
        tipo = ctx.tipo().getText()
        ids = ctx.listaIds().getText().split(',')

        for id in ids:
            if self.inFunction and id in self.symbolTableLocal:
                raise ErroDeclaracaoJaFeita(ctx.start.line, id)
            if id in self.symbolTable:
                raise ErroDeclaracaoJaFeita(ctx.start.line, id)
            if ctx.tipo().getText() == '<missing <INVALID>>':
                raise ErroTipoNaoInformado(ctx.start.line, id)
            if self.inFunction:
                self.symbolTableLocal[id] = [tipo, None]
            else:
                self.symbolTable[id] = [tipo, None]
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#decVar.
    def exitDecVar(self, ctx:trabalhoFinal_lucasParser.DecVarContext):
        if self.inFunction:
            for id in ctx.listaIds().getText().split(','):
                del self.symbolTableLocal[id]
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#decConst.
    def enterDecConst(self, ctx:trabalhoFinal_lucasParser.DecConstContext):
        tipo = ctx.tipo().getText()
        for atrib in ctx.listaAtrib().atrib():
            id_token = atrib.ID().getText()
            if self.inFunction and id_token in self.symbolTableLocal:
                raise ErroDeclaracaoJaFeita(ctx.start.line, id_token)
            if id_token in self.symbolTable:
                raise ErroDeclaracaoJaFeita(ctx.start.line, id_token)
            if ctx.tipo().getText() == '<missing <INVALID>>':
                raise ErroTipoNaoInformado(ctx.start.line, id_token)
            valor = atrib.dado().getText()
            self.symbolTable[id_token] = [tipo, valor]

            if tipo == 'int' and not atrib.dado().INT():
                raise ErroTipoIncompativelDecl(ctx.start.line, tipo)
            elif tipo == 'real' and not atrib.dado().REAL():
                raise ErroTipoIncompativelDecl(ctx.start.line, tipo)
            elif tipo == 'bool' and not atrib.dado().BOOL():
                raise ErroTipoIncompativelDecl(ctx.start.line, tipo)
            elif tipo == 'String' and not atrib.dado().STRING():
                raise ErroTipoIncompativelDecl(ctx.start.line, tipo)
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#decConst.
    def exitDecConst(self, ctx:trabalhoFinal_lucasParser.DecConstContext):
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
        func_name = ctx.ID().getText()
        func_type = 'void' if not ctx.tipo() else ctx.tipo().getText()

        # verificando se a função já foi declarada
        if func_name in self.symbolTable:
            raise ValueError(f"A função '{func_name}' já foi declarada anteriormente.")

        # criando um novo escopo local para a função
        self.symbolTableLocal = {}
        self.inFunction = True
        self.currentFunctionType = None
        if ctx.tipo():
            self.currentFunctionType = func_type

        # adicionando os parâmetros da função na tabela de símbolos local
        params_node = ctx.parametros()
        if params_node is not None:
            params = params_node.tipo()
            for param in params:
                param_type = param.getText()
                param_name = param.parentCtx.ID()[params.index(param)].getText()

                if param_name in self.symbolTableLocal:
                    raise ValueError(f"O parâmetro '{param_name}' já foi declarado anteriormente.")

                self.symbolTableLocal[param_name] = param_type

        # adicionando a função na tabela de símbolos global
        self.symbolTable[func_name] = {
            'type': func_type,
            'params': list(self.symbolTableLocal.keys())
        }
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#decFuncao.
    def exitDecFuncao(self, ctx: trabalhoFinal_lucasParser.DecFuncaoContext):
        self.inFunction = False
        self.symbolTableLocal.clear()
        self.currentFunctionType = None
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#parametros.
    def enterParametros(self, ctx:trabalhoFinal_lucasParser.ParametrosContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#parametros.
    def exitParametros(self, ctx:trabalhoFinal_lucasParser.ParametrosContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#main.
    def enterMain(self, ctx:trabalhoFinal_lucasParser.MainContext):
        self.inFunction = True
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#main.
    def exitMain(self, ctx:trabalhoFinal_lucasParser.MainContext):
        self.inFunction = False
        self.symbolTableLocal.clear()
        self.currentFunctionType = None
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
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#for.
    def exitFor(self, ctx:trabalhoFinal_lucasParser.ForContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#while.
    def enterWhile(self, ctx:trabalhoFinal_lucasParser.WhileContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#while.
    def exitWhile(self, ctx:trabalhoFinal_lucasParser.WhileContext):
        pass


    # Enter a parse tree produced by trabalhoFinal_lucasParser#return.
    def enterReturn(self, ctx:trabalhoFinal_lucasParser.ReturnContext):
        if not self.inFunction:  # se não há uma função ativa
            raise ErroRetorno(ctx.start.line)
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#return.
    def exitReturn(self, ctx: trabalhoFinal_lucasParser.ReturnContext):
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
    def enterAddMinusOp(self, ctx: trabalhoFinal_lucasParser.AddMinusOpContext):
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
    def enterIntDado(self, ctx: trabalhoFinal_lucasParser.IntDadoContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#intDado.
    def exitIntDado(self, ctx: trabalhoFinal_lucasParser.IntDadoContext):
        pass

    # Enter a parse tree produced by trabalhoFinal_lucasParser#realDado.
    def enterRealDado(self, ctx: trabalhoFinal_lucasParser.RealDadoContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#realDado.
    def exitRealDado(self, ctx: trabalhoFinal_lucasParser.RealDadoContext):
        pass

    # Enter a parse tree produced by trabalhoFinal_lucasParser#stringDado.
    def enterStringDado(self, ctx: trabalhoFinal_lucasParser.StringDadoContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#stringDado.
    def exitStringDado(self, ctx: trabalhoFinal_lucasParser.StringDadoContext):
        pass

    # Enter a parse tree produced by trabalhoFinal_lucasParser#boolDado.
    def enterBoolDado(self, ctx: trabalhoFinal_lucasParser.BoolDadoContext):
        pass

    # Exit a parse tree produced by trabalhoFinal_lucasParser#boolDado.
    def exitBoolDado(self, ctx: trabalhoFinal_lucasParser.BoolDadoContext):
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