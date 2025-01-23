import { Button } from '@arco-design/web-react';
import React from 'react';


export function getColumns(
  callback: (record: Record<string, any>, type: string) => Promise<void>
) {
  return [
    {
      title: '中文名称',
      dataIndex: 'chnName',
    },
    {
      title: '英文名称',
      dataIndex: 'engName',
    },
    {
      title: '英文缩写',
      dataIndex: 'engAbbr',
    },
    {
      title: '是否标准用语',
      dataIndex: 'stdTermFlag',
      render: (value: boolean) => {
        return value ? '是' : '否'
      }
    },
    {
      title: '操作',
      headerCellStyle: { paddingLeft: '15px' },
      render: (_, record) => (
        <Button
          type="text"
          size="small"
          onClick={() => callback(record, 'view')}
        >
          查看
        </Button>
      ),
    },
  ]
}