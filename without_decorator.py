class AbstractBlock:
    """ Абстрактный блок
    """

    def draw(self):
        raise NotImplementedError();


class TerminatorBlock(AbstractBlock):
    """ Терминальный блок (начало/конец, вход/выход)
    """

    def draw(self):
        print("Terminator block drawing ... ")


class ProcessBlock(AbstractBlock):
    """ Блок - процесс (один или несколько операторов)
    """

    def draw(self):
        print("Process block drawing ... ")


class AbstractBlockPlusLabel(AbstractBlock):
    """ Абстракный декоратор блоков
    """

    def __init__(self, decoratee, label):
        # _decoratee - ссылка на декорируемый объект
        self._decoratee = decoratee
        self._label = label

    def draw(self):
        self._decoratee.draw()
        self._drawLabel()

    def _drawLabel(self):
        print(" ... drawing label " + self._label)


class AbstractBlockPlusBorder(AbstractBlock):
    """ Абстракный декоратор блоков
    """

    def __init__(self, decoratee, border):
        # _decoratee - ссылка на декорируемый объект
        self._decoratee = decoratee
        self._border = border

    def draw(self):
        self._decoratee.draw()
        self._drawBorder()

    def _drawBorder(self):
        print(" ... drawing border " + str(self._border))

class AbstractBlockPlusLabelAndBorder(AbstractBlock):
    """ Абстракный декоратор блоков
    """

    def __init__(self, decoratee, border, label):
        # _decoratee - ссылка на декорируемый объект
        self._decoratee = decoratee
        self._border = border
        self._label = label

    def draw(self):
        self._decoratee.draw()
        self._drawBorder()
        self._drawLabel()

    def _drawBorder(self):
        print(" ... drawing border " + str(self._border))

    def _drawLabel(self):
        print(" ... drawing label " + self._label)

# терминальный блок
tBlock = TerminatorBlock()
# блок - процесс
pBlock = ProcessBlock()

plusLabel = AbstractBlockPlusLabel(tBlock, "Label222")
# Применим LabelDecorator к терминальному блоку
labelAndBorder = AbstractBlockPlusLabelAndBorder(tBlock, 22,  "Label222")


# Применим BorderDecorator к блоку - процессу
plusBorder = AbstractBlockPlusBorder(pBlock, 22)

plusLabel.draw()
labelAndBorder.draw()
plusBorder.draw()