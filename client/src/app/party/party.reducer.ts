import { PartyActions } from './party.actions';

export interface IParty {
  date?: string;
  loading: boolean;
  error?: any;
}

const INITIAL_STATE: IParty = {
  date: null,
  loading: false,
  error: null,
};

export function partyReducer(
    state: IParty = INITIAL_STATE,
    action // TODO: IPayloadAction interface
  ): IParty {
  switch (action.type) {
    case PartyActions.TEST_ACTION:
      return {
        date: new Date().toString(),
        loading: false,
        error: null,
      };
  }

  return state;
}
