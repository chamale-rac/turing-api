class Transition:
    def __init__(self, initialState: str, initialMemCacheValue: str, tapeInput: str, finalState: str, finalMemCacheValue: str, tapeOutput: str, tapeDisplacement: int) -> None:
        self.initialState: str = initialState
        self.initialMemCacheValue: str = initialMemCacheValue
        self.tapeInput: str = tapeInput
        self.finalState: str = finalState
        self.finalMemCacheValue: str = finalMemCacheValue
        self.tapeOutput: str = tapeOutput
        self.tapeDisplacement: int = tapeDisplacement

    def __eq__(self, __value: object) -> bool:
        '''
        Args: 
            __value (object): The value to compare against

        Can be compared against tuples of the form (initialState, tapeInput, memCacheValue) or other Transition objects (completeness)
        '''
        if isinstance(__value, tuple):
            if len(__value) == 3:
                return self.initialState == __value[0] and self.initialMemCacheValue == __value[1] and self.tapeInput == __value[2]
            elif len(__value) == 2:
                return self.initialState == __value[0] and self.tapeInput == __value[1]
        elif isinstance(__value, Transition):
            return self.initialState == __value.initialState and self.tapeInput == __value.tapeInput and self.initialMemCacheValue == __value.initialMemCacheValue and self.finalState == __value.finalState and self.finalMemCacheValue == __value.finalMemCacheValue and self.tapeOutput == __value.tapeOutput and self.tapeDisplacement == __value.tapeDisplacement
        return False

    def __str__(self) -> str:
        if self.tapeDisplacement == -1:
            tapeDisplacement = 'L'
        elif self.tapeDisplacement == 1:
            tapeDisplacement = 'R'
        else:
            tapeDisplacement = 'S'
        return f'sigma([{self.initialState}, {self.initialMemCacheValue}], {self.tapeInput}) = ([{self.finalState}, {self.finalMemCacheValue}], {self.tapeOutput}, {tapeDisplacement})'