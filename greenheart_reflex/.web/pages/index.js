
/** @jsxImportSource @emotion/react */import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Avatar, Box, Button, Center, Flex, Heading, HStack, Image as ChakraImage, Link, SimpleGrid, Spacer, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Box>
  <HStack sx={{"position": "sticky", "bg": "#474973", "paddingX": "2em", "paddingY": "1em", "zIndex": "999", "top": "0"}}>
  <Box sx={{"fontFamily": "Comfortaa", "fontWeight": "500", "fontSize": "1.5em"}}>
  <Text as={`span`} sx={{"color": "white"}}>
  {`i`}
</Text>
  <Text as={`span`} sx={{"color": "#B2D8B2"}}>
  {`Green`}
</Text>
  <Text as={`span`} sx={{"color": "white"}}>
  {`Heart`}
</Text>
</Box>
</HStack>
  <Center>
  <VStack sx={{"maxWidth": "600px", "width": "100%", "marginY": "2em", "padding": "2em"}}>
  <VStack alignItems={`start`} spacing={`2em`} sx={{"width": "100%"}}>
  <HStack spacing={`1em`}>
  <Avatar name={`Green Heart`} size={`xl`} src={`logo.jpg`} sx={{"color": "#E3E3E3", "bg": "#474973", "padding": "2px", "border": "4px", "borderColor": "#B2D8B2"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`}>
  <Heading size={`xl`} sx={{"size": "lg", "color": "#f2fff1", "fontFamily": "Poppins", "fontWeight": "700"}}>
  {`Juan Cruz Bogado`}
</Heading>
  <Text sx={{"marginTop": "0px !important", "color": "#E3E3E3", "fontSize": "1em", "fontFamily": "Poppins", "fontWeight": "200"}}>
  {`iGreenHeart`}
</Text>
  <HStack sx={{"color": "#B2D8B2"}}>
  <Link as={NextLink} href={`https://www.instagram.com/juanchidsm/?hl=es`} isExternal={true} sx={{"textDecoration": "none", "_hover": {}}}>
  <ChakraImage alt={`Instagram`} src={`icons/instagram.svg`} sx={{"width": "2em"}}/>
</Link>
  <Link as={NextLink} href={`https://github.com/iGreenHeart`} isExternal={true} sx={{"textDecoration": "none", "_hover": {}}}>
  <ChakraImage alt={`Github`} src={`icons/github.svg`} sx={{"width": "2em"}}/>
</Link>
  <Link as={NextLink} href={`https://ketoivy.mercadoshops.com.ar`} isExternal={true} sx={{"textDecoration": "none", "_hover": {}}}>
  <ChakraImage alt={`Keto Ivy`} src={`icons/ketoivy.png`} sx={{"width": "2em"}}/>
</Link>
</HStack>
</VStack>
</HStack>
  <Flex sx={{"width": "100%"}}>
  <Box>
  <Link as={NextLink} href={`https://www.unsam.edu.ar/escuelas/ecyt/107/ciencia/programacion-informatica`} sx={{"fontWeight": "bold", "color": "#B2D8B2", "textDecoration": "none", "_hover": {}}}>
  {`CARRERA`}
</Link>
  <Link as={NextLink} href={`https://www.unsam.edu.ar/escuelas/ecyt/107/ciencia/programacion-informatica`} sx={{"fontSize": "1em", "color": "#E3E3E3", "textDecoration": "none", "_hover": {}}}>
  {` TPI UNSAM`}
</Link>
</Box>
  <Spacer/>
  <Box sx={{"fontSize": "1em", "color": "#E3E3E3", "fontFamily": "Poppins", "fontWeight": "200"}}>
  <Text as={`span`} sx={{"color": "#B2D8B2", "fontFamily": "Poppins", "fontWeight": "500"}}>
  {`LENGUAJES`}
</Text>
  {` Python`}
</Box>
  <Spacer/>
  <Box sx={{"fontSize": "1em", "color": "#E3E3E3", "fontFamily": "Poppins", "fontWeight": "200"}}>
  <Text as={`span`} sx={{"color": "#B2D8B2", "fontFamily": "Poppins", "fontWeight": "500"}}>
  {`DB`}
</Text>
  {` MongoDB, SQL`}
</Box>
</Flex>
  <Text sx={{"fontSize": "1em", "color": "#E3E3E3"}}>
  {`Hola! Soy Juan, argentino actualmente estudiando una tecnicatura en programación informática
            en la Universidad Nacional de San Martín (UNSAM). Esta web está hecha con python puro y Reflex. Como objetivo,
            quiero como programador Backend utilizando mis habilidades y mi amor por codear para contribuir en proyectos de
            desarrollo en software.
            `}
</Text>
</VStack>
  <VStack spacing={`0.8em`} sx={{"width": "100%"}}>
  <Heading size={`lg`} sx={{"width": "100%", "paddingTop": "1em", "size": "lg", "color": "#f2fff1", "fontFamily": "Poppins", "fontWeight": "700"}}>
  {`Proyectos`}
</Heading>
  <Link as={NextLink} href={`https://github.com/iGreenHeart/typing-game-asm`} isExternal={true} sx={{"width": "100%", "textDecoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "color": "#f2fff1", "backgroundColor": "#474973", "whiteSpace": "normal", "textAling": "start", "_hover": {"backgroundColor": "#4779c4"}}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`typing_game_asm`} src={`icons/unsamlogo.png`} sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} sx={{"margin": "0px !important", "paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontFamily": "Poppins", "fontWeight": "700", "fontSize": "1.5em", "color": "#f2fff1"}}>
  {`typing_game_asm`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontWeight": "200", "fontSize": "1em", "color": "#E3E3E3"}}>
  {`Proyecto Final de Sistemas de Procesamiento de Datos`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Heading size={`lg`} sx={{"width": "100%", "paddingTop": "1em", "size": "lg", "color": "#f2fff1", "fontFamily": "Poppins", "fontWeight": "700"}}>
  {`Contacto`}
</Heading>
  <Link as={NextLink} href={`mailto:juancbogadoo@gmail.com`} isExternal={true} sx={{"width": "100%", "textDecoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "color": "#f2fff1", "backgroundColor": "#474973", "whiteSpace": "normal", "textAling": "start", "_hover": {"backgroundColor": "#4779c4"}}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Email`} src={`icons/envelope-solid.svg`} sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} sx={{"margin": "0px !important", "paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontFamily": "Poppins", "fontWeight": "700", "fontSize": "1.5em", "color": "#f2fff1"}}>
  {`Email`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontWeight": "200", "fontSize": "1em", "color": "#E3E3E3"}}>
  {`juancbogadoo@gmail.com`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://www.linkedin.com/in/bogado-juan-cruz-0744b8246/`} isExternal={true} sx={{"width": "100%", "textDecoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "color": "#f2fff1", "backgroundColor": "#474973", "whiteSpace": "normal", "textAling": "start", "_hover": {"backgroundColor": "#4779c4"}}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Linkedin`} src={`icons/linkedin.svg`} sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} sx={{"margin": "0px !important", "paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontFamily": "Poppins", "fontWeight": "700", "fontSize": "1.5em", "color": "#f2fff1"}}>
  {`Linkedin`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontWeight": "200", "fontSize": "1em", "color": "#E3E3E3"}}>
  {`Curriculum y mensajeria`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
</VStack>
</VStack>
</Center>
  <VStack spacing={`1em`} sx={{"marginBottom": "2em", "paddingBottom": "2em", "paddingX": "2em", "color": "#f2fff1"}}>
  <SimpleGrid columns={[1, 2]} spacing={`2em`}>
  <ChakraImage alt={`Logotipo de GreenHeart`} src={`logo.jpg`} sx={{"height": "4em", "width": "4em", "borderRadius": "50%"}}/>
  <ChakraImage alt={`Logotipo de UNSAM`} src={`Logo_UNSAM.ico`} sx={{"height": "4em", "bg": "White"}}/>
</SimpleGrid>
  <Text sx={{"fontSize": "0.8em"}}>
  {`@2022 - 2023 hecho por Juan Cruz Bogado V0.1`}
</Text>
  <Text sx={{"fontSize": "0.8em", "marginTop": "0px !important"}}>
  {`Coding with love from Argentina`}
</Text>
</VStack>
</Box>
  <NextHead>
  <title>
  {`GreenHeart's Page`}
</title>
  <meta content={`Hola! Soy GreenHeart, Futuro técnico en programación y programador en backend.`} name={`description`}/>
  <meta content={`logo.jpg`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
