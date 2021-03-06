import styled from "styled-components";
import { Container, FormControl, FormLabel, Button } from "react-bootstrap";

const white = "#fff";
const darkblue = "#5C5CFF";
const lightblue = "#03a9f4";
const lavender = "#eeb4ff";

export const RegisterContainer = styled(Container)`
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: ${lavender};
  max-width: 100%;
`;

export const DarkBlueCard = styled.div`
  background-color: ${darkblue};
  border-radius: 10px;
  box-shadow: 0px 6px 6px rgba(0, 0, 0, 0.14), 0px 6px 9px rgba(0, 0, 0, 0.12),
    6px 6px 9px rgba(0, 0, 0, 0.2);
  padding: 5px 1rem;
`;

export const CardContent = styled.div`
  flex: 1 1 auto;
  min-height: 1px;
  padding: 1.25rem 5px;
`;

export const ContentWrapper = styled.div`
  width: 300px;
`;

export const Header = styled.h2`
  text-align: center;
  margin-bottom: 4px;
  color: ${white};
  padding-bottom: 1rem;
`;

export const WhiteFormLabel = styled(FormLabel)`
  color: ${white};
  font-size: 18px;
`;
export const Textbox = styled(FormControl)`
  background-color: ${lavender};
  &:focus {
    border-color: ${darkblue};
    box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(133, 63, 63, 0.6);
    }
    background-color: ${lavender};
    color: ${darkblue};
  }
  color: ${darkblue};
  font-size: 18px;
  font-weight: 600;
`;

export const SignInText = styled.div`
  text-align: center;
  margin-top: 10px;
  width: 100%;
  color: white;
`;

export const ForgotPassword = styled(SignInText)`
  color: ${white};
  &:hover {
    text-decoration: none;
  }
`;

export const SubmitButton = styled(Button)`
  background-color: ${lightblue};
  border-color: ${lightblue};
  &:hover {
    background-color: ${lavender};
    border-color: ${lavender};
    color: #222;
  }
  width: 100%;
  margin-top: 4px;
`;

export const BottomLinkText = styled.span`
  color: white;
  font-weight: bold;
`