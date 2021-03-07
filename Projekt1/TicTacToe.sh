#!/bin/bash

BOARD=("0" "0" "0" "0" "0" "0" "0" "0" "0")
PLAYER="2"
IS_WIN="0"

function printBoard {
  clear
  echo "${BOARD[0]} | ${BOARD[1]} | ${BOARD[2]}"
  echo "${BOARD[3]} | ${BOARD[4]} | ${BOARD[5]}"
  echo "${BOARD[6]} | ${BOARD[7]} | ${BOARD[8]}"
}

checkIfGameEnded() {
  # tbd
  true
}

changePlayer() {
  if [ ${PLAYER} -eq 1 ]; then
    PLAYER="2"
  else
    PLAYER="1"
  fi
}

verifyPosition() {
  local COLUMN=$1
  local ROW=$2
  echo "COLUMN ${COLUMN}"
  echo "ROW ${ROW}"
  if [ "${BOARD[${ROW} + ${COLUMN} * 2]}" == "0" ]; then
    return 0
  else
    return 255
  fi
}

updateBoard() {
  local COLUMN=$1
  local ROW=$2
  local SIGN=$([ "$PLAYER" == 1 ] && echo "#" || echo "@")

  BOARD[${ROW} + ${COLUMN} * 2]=${SIGN}

}

while [ $IS_WIN -eq 0 ];
 do
  printBoard
  echo -e "\n Ruch gracza  ${PLAYER}"
  echo -e "\n Podaj kolumne ${PLAYER}"
  read COLUMN
  echo -e "\n Podaj wiersz ${PLAYER}"
  read ROW
  if verifyPosition "${COLUMN}" "${ROW}" -eq 0; then
    updateBoard "${COLUMN}" "${ROW}"
    changePlayer
    checkIfGameEnded

  else
    read -p "To pole jest juz zajete, wybierz inne - nacisnij dowolny klawisz by kontynuowac"
  fi
done

