import {
    convertToAD,
    convertToBS,
    IYearMonthDate,
    IAdBs,
    format,
    Language,
    parse
} from './constant'

const dateSymbol = Symbol('Date')
const daySymbol = Symbol('Day')
const yearSymbol = Symbol('Year')
const monthSymbol = Symbol('MonthIndex')
const jsDateSymbol = Symbol('JsDate')
const convertToBSMethod = Symbol('convertToBS()')
const convertToADMethod = Symbol('convertToAD()')
const setAdBs = Symbol('setADBS()')
const setDayYearMonth = Symbol('setDayYearMonth()')

export default class NepaliDate {
    private [jsDateSymbol]: Date
    private [yearSymbol]: number
    private [dateSymbol]: number
    private [daySymbol]: number
    private [monthSymbol]: number

    static language: 'np' | 'en' = Language.en
    constructor(value?: string | number | Date)
    constructor(year: number, monthIndex: number, date: number)
    constructor() {
        const constructorError = new Error('Invalid constructor arguments')
        // if (arguments.length === 0) {
        //   this[convertToBSMethod](new Date())
        // } else if (arguments.length === 1) {
        //   const argument = arguments[0]
        //   switch (typeof argument) {
        //     case 'number':
        //       this[convertToBSMethod](new Date(argument))
        //       break
        //     case 'string':
        //       const { date, year, month } = parse(argument)
        //       this[setDayYearMonth](year, month, date)
        //       this[convertToADMethod]()
        //       break
        //     case 'object':
        //       if (argument instanceof Date) {
        //         this[convertToBSMethod](argument)
        //       } else {
        //         throw constructorError
        //       }
        //       break
        //     default:
        //       throw constructorError
        //   }
        // } else if (arguments.length <= 3) {
        //   this[setDayYearMonth](arguments[0], arguments[1], arguments[2])
        //   this[convertToADMethod]()
        // } else {
        //   throw constructorError
        // }
      }
}