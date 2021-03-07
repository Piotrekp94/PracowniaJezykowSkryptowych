#!/bin/bash

BOARD=("0" "0" "0" "0" "0" "0" "0" "0" "0")
PLAYER="2"
CONTINUE_GAME="0"

function printBoard {
  clear
  echo "${BOARD[0]} | ${BOARD[1]} | ${BOARD[2]}"
  echo "${BOARD[3]} | ${BOARD[4]} | ${BOARD[5]}"
  echo "${BOARD[6]} | ${BOARD[7]} | ${BOARD[8]}"
}
isHorizontal() {
  for i in {0..2}; do
    if [ "${BOARD[i * 3]}" -ne 0 ]; then
      if [[ "${BOARD[i * 3]}" -eq "${BOARD[i * 3 + 1]}" && "${BOARD[i * 3]}" -eq "${BOARD[i * 3 + 1]}" ]]; then
        return 0
      fi
    fi
  done
  return 1
}

isDiagonal() {
  if [ "${BOARD[4]}" -eq 0 ]; then
    return 1
  fi
  [[ "${BOARD[0]}" -eq "${BOARD[4]}" && "${BOARD[0]}" -eq "${BOARD[8]}" ]] || [[ ${BOARD[2]} -eq ${BOARD[4]} && ${BOARD[2]} -eq ${BOARD[6]} ]]
}

isVertical() {
  for i in {0..2}; do
    if [ "${BOARD[i]}" -ne 0 ]; then
      if [[ "${BOARD[i]}" -eq "${BOARD[i + 3]}" && "${BOARD[i]}" -eq "${BOARD[i + 6]}" ]]; then
        return 0
      fi
    fi
  done
  return 1
}

checkIfGameEnded() {
  isDiagonal || isHorizontal || isVertical
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
  [ "${BOARD[${ROW} * 3 + ${COLUMN}]}" == "0" ]
}

updateBoard() {
  local COLUMN=$1
  local ROW=$2
  local SIGN
  SIGN=$([ "$PLAYER" == 1 ] && echo "1" || echo "2")

  BOARD[${ROW} * 3 + ${COLUMN}]=${SIGN}

}

while [ $CONTINUE_GAME -eq 0 ]; do
  printBoard
  echo -e "\nRuch gracza  ${PLAYER}"
  echo -e "Podaj indeks kolumny [0-2]:"
  read COLUMN
  echo -e "Podaj indeks wiersza [0-2]:"
  read ROW
  if verifyPosition "${COLUMN}" "${ROW}" -eq 0; then
    echo "${COLUMN}" "${ROW}"
    updateBoard "${COLUMN}" "${ROW}"
    changePlayer
    if checkIfGameEnded -eq 0; then
      CONTINUE_GAME=1
    fi
  else
    read -p "To pole jest juz zajete, wybierz inne - nacisnij dowolny klawisz by kontynuowac"
  fi
done
