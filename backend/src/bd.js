import {createPool} from 'mysql2/promise';


// Conexion a la base de datos
export const pool = createPool({    
    host: 'localhost',
    user:  'root',
    password: 'rootpass',
    port: 3306,
    database: 'joyeria'
});